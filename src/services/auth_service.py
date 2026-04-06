from __future__ import annotations

from src.clients.auth_client import AuthClient
from src.schemas.auth_schema import LOGIN_RESPONSE_SCHEMA, ME_RESPONSE_SCHEMA
from src.utils.assertions import assert_status_code
from src.utils.schema_validator import validate_schema


class AuthService:
    def __init__(self, client: AuthClient) -> None:
        self.client = client

    def login_and_validate(self, credentials: dict):
        response = self.client.login(credentials)
        assert_status_code(response, 200)

        response_json = response.json()
        validate_schema(response_json, LOGIN_RESPONSE_SCHEMA)
        return response

    def get_me_and_validate(self):
        response = self.client.me()
        assert_status_code(response, 200)

        response_json = response.json()
        validate_schema(response_json, ME_RESPONSE_SCHEMA)
        return response