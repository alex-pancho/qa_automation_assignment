"""
Autobuilds API endpoint class
"""
from dataclasses import dataclass
from typing import Any
from api.endpoints.endpoint import Endpoint


@dataclass
class Posts_Post_Body:
    """Request body for posts POST operation."""

    title: str
    body: str
    userId: int

@dataclass
class Posts_Id_Put_Body:
    """Request body for posts_id PUT operation."""

    id: int
    title: str
    body: str
    userId: int

@dataclass
class Posts_Id_Patch_Body:
    """Request body for posts_id PATCH operation."""

    title: str = None
    body: str = None
    userId: int = None

@dataclass
class Default:
    """
    Autobuild class
    """

    @property
    def posts_get(self) -> Endpoint:
        """
        Returns a list of posts. Supports filtering by userId.

        """
        method = "GET"
        endpoint = "/posts"
        return Endpoint(method, endpoint)

    @property
    def posts_post(self) -> Endpoint:
        """
        Creates a new post (fake creation).

        """
        method = "POST"
        endpoint = "/posts"
        body = Posts_Post_Body
        return Endpoint(method, endpoint, body)

    @property
    def posts_id_get(self) -> Endpoint:
        """
        Get post by ID

        """
        method = "GET"
        endpoint = "/posts/{id}"
        return Endpoint(method, endpoint)

    @property
    def posts_id_put(self) -> Endpoint:
        """
        Fully updates a post (fake update).

        """
        method = "PUT"
        endpoint = "/posts/{id}"
        body = Posts_Id_Put_Body
        return Endpoint(method, endpoint, body)

    @property
    def posts_id_patch(self) -> Endpoint:
        """
        Partially updates a post (fake update).

        """
        method = "PATCH"
        endpoint = "/posts/{id}"
        body = Posts_Id_Patch_Body
        return Endpoint(method, endpoint, body)

    @property
    def posts_id_delete(self) -> Endpoint:
        """
        Deletes a post (fake delete).

        """
        method = "DELETE"
        endpoint = "/posts/{id}"
        return Endpoint(method, endpoint)

    @property
    def posts_id_comments_get(self) -> Endpoint:
        """
        Get comments for a post

        """
        method = "GET"
        endpoint = "/posts/{id}/comments"
        return Endpoint(method, endpoint)
