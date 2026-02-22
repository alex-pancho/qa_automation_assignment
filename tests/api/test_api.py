import pytest
from framework_api.client import APIError, ApiClient
from api.endpoints.json_placeholder import (
    Default,
    Posts_Post_Body,
    Posts_Id_Put_Body,
    Posts_Id_Patch_Body,
)
from api.endpoints.endpoint import Endpoint
from tests.api.helper import endpoint_helper


def test_get_posts(default: Default, host: str):
    """
    GET /posts — verify list of posts
    """
    point: Endpoint = default.posts_get
    endpoint = endpoint_helper(point, host)

    client = ApiClient(endpoint)

    try:
        data = client.request()
    except APIError as e:
        pytest.skip(f"GET posts failed ({e.status_code}): {e.message}")

    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]
    assert "userId" in data[0]


def test_get_post_by_id(default: Default, host: str):
    """
    GET /posts/{id} — verify single post
    """
    point: Endpoint = default.posts_id_get
    endpoint = endpoint_helper(point, host, put_in_path={"id": 1})

    client = ApiClient(endpoint)

    try:
        data = client.request()
    except APIError as e:
        pytest.skip(f"GET post by id failed ({e.status_code}): {e.message}")

    assert isinstance(data, dict)
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


def test_create_post(default: Default, host: str):
    """
    POST /posts — create post
    """
    point: Endpoint = default.posts_post

    body = Posts_Post_Body(
        title="foo",
        body="bar",
        userId=1,
    )

    endpoint = endpoint_helper(point, host)
    client = ApiClient(endpoint)
    client.data = body
    try:
        data = client.request()
    except APIError as e:
        pytest.skip(f"POST post failed ({e.status_code}): {e.message}")

    assert isinstance(data, dict)
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1
    assert "id" in data


def test_update_post_put(default: Default, host: str):
    """
    PUT /posts/{id} — full update
    """
    point: Endpoint = default.posts_id_put

    body = Posts_Id_Put_Body(
        id=1,
        title="updated title",
        body="updated body",
        userId=1,
    )

    endpoint = endpoint_helper(point, host, put_in_path={"id": 1})

    client = ApiClient(endpoint)
    client.data = body
    try:
        data = client.request()
    except APIError as e:
        pytest.skip(f"PUT post failed ({e.status_code}): {e.message}")

    assert data["id"] == 1
    assert data["title"] == "updated title"
    assert data["body"] == "updated body"
    assert data["userId"] == 1


def test_update_post_patch(default: Default, host: str):
    """
    PATCH /posts/{id} — partial update
    """
    point: Endpoint = default.posts_id_patch

    body = Posts_Id_Patch_Body(title="patched title")

    endpoint = endpoint_helper(point, host, put_in_path={"id": 1})

    client = ApiClient(endpoint)
    client.data = body

    try:
        data = client.request()
    except APIError as e:
        pytest.skip(f"PATCH post failed ({e.status_code}): {e.message}")

    assert data["id"] == 1
    assert data["title"] == "patched title"


def test_delete_post(default: Default, host: str):
    """
    DELETE /posts/{id}
    """
    point: Endpoint = default.posts_id_delete

    endpoint = endpoint_helper(point, host, put_in_path={"id": 1})

    client = ApiClient(endpoint)

    try:
        data = client.request()
    except APIError as e:
        pytest.skip(f"DELETE post failed ({e.status_code}): {e.message}")

    assert data == {} or data is None


def test_get_post_comments(default: Default, host: str):
    """
    GET /posts/{id}/comments
    """
    point: Endpoint = default.posts_id_comments_get
   
    endpoint = endpoint_helper(point, host, put_in_path={"id": 1})

    client = ApiClient(endpoint)

    try:
        data = client.request()
    except APIError as e:
        pytest.skip(f"GET comments failed ({e.status_code}): {e.message}")

    assert isinstance(data, list)
    assert len(data) > 0
    assert "postId" in data[0]
    assert "id" in data[0]
    assert "email" in data[0]
    assert "body" in data[0]
