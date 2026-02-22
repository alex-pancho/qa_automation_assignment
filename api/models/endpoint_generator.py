#!/usr/bin/env python3
import sys
import re
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def sanitize_class_name(name: str) -> str:
    """
    Make pytinic names for class

    :param name: Python/Pep CamelCase
    :type name: str
    :return: Python_Pep_CamelCase
    :rtype: str
    """
    name = re.sub(r"[^0-9a-zA-Z]+", " ", name).title().replace(" ", "_")
    if not name or name[0].isdigit():
        name = "C" + name
    return name


def sanitize_method_name(path: str) -> str:
    """
    Make pytinic names for def

    :param name: Python/Pep CamelCase
    :type name: str
    :return: python_pep_snake_case
    :rtype: str
    """
    name = path.strip("/")
    name = re.sub(r"[^0-9a-zA-Z]+", "_", name).strip("_").lower()
    if not name or name[0].isdigit():
        name = "op_" + name
    return name


def first_content_type(request_body: dict | None) -> str | None:
    if not request_body:
        return None
    content = request_body.get("content") or {}
    return next(iter(content.keys()), None) if content else None


def resolve_schema_ref(ref: str, openapi: dict) -> dict:
    """
    Resolve $ref to actual schema definition.

    :param ref: Reference string like '#/components/schemas/CarWriteRequest'
    :type ref: str
    :param openapi: OpenAPI specification dict
    :type openapi: dict
    :return: Resolved schema dict
    :rtype: dict
    """
    if not ref.startswith("#/"):
        return {}

    parts = ref.lstrip("#/").split("/")
    obj = openapi

    for part in parts:
        if isinstance(obj, dict):
            obj = obj.get(part, {})
        else:
            return {}

    return obj if isinstance(obj, dict) else {}


def get_body_schema(request_body: dict | None, openapi: dict) -> dict:
    """
    Extract body schema from request body, resolving references if needed.

    :param request_body: Request body specification
    :type request_body: dict | None
    :param openapi: OpenAPI specification
    :type openapi: dict
    :return: Schema definition
    :rtype: dict
    """
    if not request_body:
        return {}

    content = request_body.get("content") or {}
    for _, cval in content.items():
        schema = cval.get("schema") or {}

        # Handle $ref
        if "$ref" in schema:
            return resolve_schema_ref(schema["$ref"], openapi)

        return schema

    return {}


def schema_properties(request_body: dict | None) -> dict:
    props = {}
    if not request_body:
        return props
    content = request_body.get("content") or {}
    for _, cval in content.items():
        schema = cval.get("schema") or {}
        properties = schema.get("properties") or {}
        for k, v in properties.items():
            props[k] = v
        break
    return props


def openapi_type_to_python(openapi_type: str, openapi_format: str | None = None) -> str:
    """
    Convert OpenAPI type to Python type annotation.

    :param openapi_type: OpenAPI type (string, integer, number, boolean, array, object)
    :type openapi_type: str
    :param openapi_format: OpenAPI format (date, date-time, email, etc.)
    :type openapi_format: str | None
    :return: Python type string
    :rtype: str
    """
    if openapi_type == "string":
        if openapi_format == "date":
            return "str"  # Could be datetime.date but str is safer for API
        elif openapi_format == "date-time":
            return "str"  # Could be datetime.datetime but str is safer for API
        elif openapi_format == "email":
            return "str"
        return "str"
    elif openapi_type == "integer":
        return "int"
    elif openapi_type == "number":
        return "float"
    elif openapi_type == "boolean":
        return "bool"
    elif openapi_type == "array":
        return "list"
    elif openapi_type == "object":
        return "dict"

    return "Any"


def extract_body_fields(request_body: dict | None, openapi: dict) -> list[dict]:
    """
    Extract body fields with their types and required status.

    :param request_body: Request body specification
    :type request_body: dict | None
    :param openapi: OpenAPI specification
    :type openapi: dict
    :return: List of field dicts with keys: name, type, required
    :rtype: list[dict]
    """
    if not request_body:
        return []

    schema = get_body_schema(request_body, openapi)
    properties = schema.get("properties") or {}
    required_fields = set(schema.get("required") or [])

    fields = []
    for field_name, field_spec in properties.items():
        field_type = field_spec.get("type", "Any")
        field_format = field_spec.get("format")
        python_type = openapi_type_to_python(field_type, field_format)

        is_required = field_name in required_fields

        fields.append(
            {
                "name": field_name,
                "type": python_type,
                "required": is_required,
                "description": field_spec.get("description", ""),
            }
        )

    return fields


def extract_method_info(path: str, op: dict, openapi: dict | None = None) -> dict:
    """Extract method information from OpenAPI operation."""
    if openapi is None:
        openapi = {}

    tags = op.get("tags") or ["Default"]
    class_name = sanitize_class_name(tags[0])

    rb = op.get("requestBody", {})
    props = list(schema_properties(rb).keys())
    body_fields = extract_body_fields(rb, openapi)

    method_name = sanitize_method_name(path)
    description = (op.get("description") or op.get("summary") or "").strip()
    ctype = first_content_type(rb) or "application/json"
    # result_1 = (
    #     (op.get("operationId", "") or "").split("_")[-1].upper()
    #     if op.get("operationId")
    #     else ""
    # )
    end_method = (list(reversed(path.split("/"))) + [""])[0].upper() or "GET"

    return {
        "class_name": class_name,
        "method_name": method_name,
        "http_method": end_method,
        "endpoint": path,
        "content_type": ctype,
        "props": props,
        "body_fields": body_fields,
        "description": description,
    }


def build_class_methods(openapi: dict) -> dict:
    """Build class methods dictionary from OpenAPI spec."""
    paths = openapi.get("paths") or {}
    class_methods = defaultdict(list)

    for path, methods in paths.items():
        for http_method, op in (methods or {}).items():
            if http_method.startswith("x-"):
                continue

            info = extract_method_info(path, op, openapi)
            info["http_method"] = http_method.upper()
            class_methods[info["class_name"]].append(info)

    return class_methods


def generate_body_dataclass(method_info: dict, ident: str) -> list:
    """Generate Python code for Body dataclass for a method."""
    lines = []

    if not method_info.get("body_fields"):
        return lines

    # Create a unique class name based on method name
    method_name = method_info["method_name"]
    http_method = method_info["http_method"].lower()
    body_class_name = sanitize_class_name(f"{method_name}_{http_method}_body")

    lines.append("@dataclass")
    lines.append(f"class {body_class_name}:")
    lines.append(
        f'{ident}"""Request body for {method_info["method_name"]} {method_info["http_method"]} operation."""'
    )
    lines.append("")

    # Separate required and optional fields to maintain dataclass field order
    required_fields = [f for f in method_info["body_fields"] if f["required"]]
    optional_fields = [f for f in method_info["body_fields"] if not f["required"]]

    # Generate required fields first
    for field in required_fields:
        field_name = field["name"]
        field_type = field["type"]
        lines.append(f"{ident}{field_name}: {field_type}")

    # Generate optional fields with defaults
    for field in optional_fields:
        field_name = field["name"]
        field_type = field["type"]
        lines.append(f"{ident}{field_name}: {field_type} = None")

    lines.append("")
    return lines


def generate_method(method_info: dict, ident: str) -> list:
    """Generate Python code for a single method."""
    lines = []
    m = method_info
    lines.append(f"{ident}@property")
    lines.append(
        f"{ident}def {m['method_name']}_{m['http_method'].lower()}(self) -> Endpoint:"
    )
    ident = ident * 2
    lines.append(f'{ident}"""')
    if m["description"]:
        lines.append(f"{ident}{m['description']}")
        lines.append("")
    lines.append(f'{ident}"""')
    lines.append(f'{ident}method = "{m["http_method"]}"')
    lines.append(f'{ident}endpoint = "{m["endpoint"]}"')

    # Generate body if request has body fields
    if m.get("body_fields"):
        method_name = m["method_name"]
        http_method = m["http_method"].lower()
        body_class_name = sanitize_class_name(f"{method_name}_{http_method}_body")
        lines.append(f"{ident}body = {body_class_name}")
        lines.append(f"{ident}return Endpoint(method, endpoint, body)")
    else:
        lines.append(f"{ident}return Endpoint(method, endpoint)")

    lines.append("")
    return lines


def generate_class(class_name: str, methods: list, ident: str) -> list:
    """Generate Python code for a single class."""
    lines = []

    # Generate Body dataclasses first (before the main class)
    body_classes = []
    for m in methods:
        body_classes.extend(generate_body_dataclass(m, ident))

    lines.extend(body_classes)

    lines.append("@dataclass")
    lines.append(f"class {class_name}:")

    lines.append(f'{ident}"""\n{ident}Autobuild class\n{ident}"""')

    if not methods:
        lines.append(f"{ident}pass")
        lines.append("")
        return lines

    lines.append("")

    for m in methods:
        lines.extend(generate_method(m, ident))

    return lines


def generate_endpoint_class():
    lines = []
    ident = "    "
    class_name = "Endpoint"
    lines.append("from dataclasses import dataclass, field")
    lines.append("from typing import Dict, Any\n\n")

    lines.append("@dataclass")
    lines.append(f"class {class_name}:")
    lines.append(
        f'{ident}"""\n{ident}Endpoint definition with method, path and optional body.\n{ident}"""'
    )
    lines.append(f"{ident}method: str")
    lines.append(f"{ident}endpoint: str")
    lines.append(f"{ident}body: Dict[str, Any] = field(default_factory=dict)\n")

    return "\n".join(lines).rstrip() + "\n"


def generate(openapi: dict) -> str:
    """Generate Python code from OpenAPI specification."""
    class_methods = build_class_methods(openapi)

    lines = []
    ident = "    "
    lines.append('"""\nAutobuilds API endpoint class\n"""')
    lines.append("from dataclasses import dataclass")
    lines.append("from typing import Any")
    lines.append("from api.endpoints.endpoint import Endpoint\n\n")

    for class_name in sorted(class_methods.keys()):
        lines.extend(generate_class(class_name, class_methods[class_name], ident))

    return "\n".join(lines).rstrip() + "\n"


def main(yaml_file: Path):
    """
    All magic lives here

    :param yaml_file: path to file
    :type yaml_file: Path
    """
    incoming_data = yaml_file.read_text(encoding="utf-8")
    data = yaml.safe_load(incoming_data)
    out_data = generate(data)
    return out_data


def save_to_file(filename: str | Path, content: str) -> None:
    """
    Save resilt to .py file

    :param filename: Description
    :type filename: str
    :param content: Description
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    wd = Path(__file__).parent
    name = sys.argv[1] if len(sys.argv) > 1 else "car_api"
    openapi_file = wd / f"{name}.yaml"
    py_text = main(openapi_file)
    pyfile = wd.parent / "endpoints" / f"{name.lower()}.py"
    save_to_file(pyfile, py_text)
    endpoint_content = generate_endpoint_class()
    endpoint_file = wd.parent / "endpoints" / "endpoint.py"
    save_to_file(endpoint_file, endpoint_content)
