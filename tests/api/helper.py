"""
Helper functions can placed here
"""
from copy import deepcopy
from api.endpoints.endpoint import Endpoint


def endpoint_helper(point: Endpoint, host: str, put_in_path: dict | None = None) -> Endpoint:
    """
    Build final endpoint with host and path params replacement.

    Example:
        endpoint = "/posts/{id}"
        host = "http://127.0.0.1"
        put_in_path = {"id": 1}
        result: "http://127.0.0.1/posts/1"
    """
    put_in_path = put_in_path or {}


    url = point.endpoint

    for key, value in put_in_path.items():
        url = url.replace(f"{{{key}}}", str(value))

    point.endpoint = host.rstrip("/") + url
    return point
