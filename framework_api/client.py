"""
Minimal, robust API client using niquests.
"""

from dataclasses import asdict, is_dataclass
from typing import Any, Dict, Optional

import niquests
from pydantic import BaseModel, ValidationError
from api.endpoints.endpoint import Endpoint


class ApiClient:
    """
    Minimal, robust API client using niquests.
    """

    @staticmethod
    def check_serialize_body(body: Any) -> Dict[str, Any]:
        """Конвертує dataclass або dict в dict для API запиту"""
        if is_dataclass(body) and not isinstance(body, type):
            return asdict(body)
        return body

    def __init__(
        self,
        endpoint: Endpoint,
        schema="",
        headers: Dict = None,
        timeout: int = 30,
        verify_ssl: bool = True,
        validate_response: bool = False,
    ) -> None:
        """
        endpoint: Endpoint dataclass object
        url = "",
        schema = "",
        headers = "",
        timeout = "",
        verify_ssl = True,
        validate_response = False,
        """
        self.session = niquests.Session()
        if headers is not None:
            self.session.headers.update(headers)
        ua_header = {
            "Accept": "application/json",
            "User-Agent": "upc-qa-api-client/1.1",
        }
        self.session.headers.update(ua_header)
        endpoint: Endpoint = endpoint
        self.url = endpoint.endpoint
        self.method = endpoint.method
        self.params: Dict[str, Any] = {}
        self.data: Dict[str, Any] = {}

        if endpoint.body:
            serialized_body = self.check_serialize_body(endpoint.body)
            if self.method.lower() == "get":
                self.params = serialized_body
            else:
                self.data = serialized_body

        self.schema = schema
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.validate_response = validate_response

    def request(self) -> Any:
        """
        Docstring for request

        :param self: Description
        :rtype: Any
        """
        try:
            resp = self.session.request(
                method=self.method,
                url=self.url,
                params=self.params,
                json=self.data,
                headers=self.session.headers,
                timeout=self.timeout,
                verify=self.verify_ssl,
            )
        except niquests.RequestException as exc:
            raise APIError(-1, str(exc)) from exc

        content_type = resp.headers.get("Content-Type", "")
        body = None
        if resp.text:
            if "application/json" in str(content_type):
                try:
                    body = resp.json()
                except ValueError:
                    body = resp.text
            else:
                body = resp.text or None

        if not resp.ok and self.validate_response:
            message = (
                body.get("error") if isinstance(body, dict) else (body or resp.reason)
            )
            raise APIError(resp.status_code, message, response=resp)
        elif self.validate_response:
            self.validate(body, self.schema)
        return body

    @staticmethod
    def validate(response_json, schema: type[BaseModel]) -> BaseModel:
        """Response pydanic validation"""
        try:
            return schema.model_validate(response_json)
        except ValidationError as e:
            raise AssertionError(f"Schema validation failed:\n{e}") from e


class APIError(Exception):
    """Raised when an API request fails (non-2xx response)."""

    def __init__(
        self,
        status_code: int | None,
        message: str | Any | None,
        response: Optional[niquests.Response] = None,
    ):
        super().__init__(f"{status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.response = response
