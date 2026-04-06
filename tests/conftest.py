from __future__ import annotations

import pytest

from src.clients.auth_client import AuthClient
from src.utils.config_reader import get_customer_credentials
from src.utils.assertions import assert_status_code


@pytest.fixture(scope="session")
def customer_credentials() -> dict:
    creds = get_customer_credentials()
    if not creds["phone_number"] or not creds["password"]:
        pytest.skip("Customer credentials are missing in .env")
    return creds


@pytest.fixture(scope="session")
def auth_client() -> AuthClient:
    return AuthClient()


@pytest.fixture(scope="session")
def customer_login_response(auth_client: AuthClient, customer_credentials: dict):
    response = auth_client.login(customer_credentials)
    assert_status_code(response.status_code, 200)
    return response


@pytest.fixture(scope="session")
def customer_tokens(customer_login_response) -> dict:
    data = customer_login_response.json()
    return data


@pytest.fixture(scope="session")
def customer_access_token(customer_tokens: dict) -> str:
    possible_keys = ["access_token", "token", "access"]
    for key in possible_keys:
        if key in customer_tokens:
            return customer_tokens[key]

    pytest.fail(f"Access token key not found in response: {customer_tokens}")


@pytest.fixture(scope="session")
def authenticated_customer_client(customer_access_token: str) -> AuthClient:
    return AuthClient(token=customer_access_token)