from __future__ import annotations

from src.utils.assertions import assert_status_code_in


class SecurityService:
    def __init__(self, client) -> None:
        self.client = client

    def assert_protected_get_requires_auth(self, endpoint: str, expected_statuses: list[int] | None = None):
        expected_statuses = expected_statuses or [401, 403]
        response = self.client.get(endpoint)
        assert_status_code_in(response, expected_statuses)
        return response

    def assert_protected_post_requires_auth(
        self,
        endpoint: str,
        payload: dict | None = None,
        expected_statuses: list[int] | None = None,
    ):
        expected_statuses = expected_statuses or [401, 403]
        response = self.client.post(endpoint, json=payload or {})
        assert_status_code_in(response, expected_statuses)
        return response

    def assert_invalid_token_rejected(
        self,
        endpoint: str,
        expected_statuses: list[int] | None = None,
    ):
        expected_statuses = expected_statuses or [401, 403]
        response = self.client.get(endpoint)
        assert_status_code_in(response, expected_statuses)
        return response