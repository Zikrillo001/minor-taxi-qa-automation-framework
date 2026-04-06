from __future__ import annotations
from src.clients.base_client import BaseClient
import pytest

from src.clients.auth_client import AuthClient
from src.utils.config_reader import debug_env_info, get_customer_credentials
from src.utils.assertions import assert_status_code


def pytest_configure(config):
    print("\n[DEBUG ENV INFO]", debug_env_info())


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
    phone = customer_credentials["phone_number"]
    password = customer_credentials["password"]

    login_attempts = [
        ("phone_number", auth_client.login_with_phone(phone, password)),
        ("phone", auth_client.login_with_phone_alt(phone, password)),
        ("username", auth_client.login_with_username(phone, password)),
        ("email", auth_client.login_with_email(phone, password)),
    ]

    for strategy_name, response in login_attempts:
        if response.status_code == 200:
            print(f"\n[LOGIN SUCCESS STRATEGY] {strategy_name}")
            return response

    debug_results = [
        (strategy, resp.status_code, resp.text[:500])
        for strategy, resp in login_attempts
    ]
    pytest.fail(f"All login strategies failed: {debug_results}")


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


@pytest.fixture(scope="session")
def invalid_token_client() -> BaseClient:
    return BaseClient(token="this.is.invalid.token")


@pytest.fixture(scope="session")
def anonymous_client() -> BaseClient:
    return BaseClient()