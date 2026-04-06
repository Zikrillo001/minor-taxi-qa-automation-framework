import pytest

from src.clients.auth_client import AuthClient
from src.utils.assertions import assert_status_code_in


@pytest.mark.negative
@pytest.mark.auth
def test_login_with_invalid_password(customer_credentials):
    client = AuthClient()

    payload = {
        "phone_number": customer_credentials["phone_number"],
        "password": "wrong_password_123",
    }

    response = client.login(payload)
    assert_status_code_in(response, [400, 401, 403])


@pytest.mark.negative
@pytest.mark.auth
def test_login_with_missing_password(customer_credentials):
    client = AuthClient()

    payload = {
        "phone_number": customer_credentials["phone_number"],
    }

    response = client.login(payload)
    assert_status_code_in(response, [400, 401, 422])


@pytest.mark.negative
@pytest.mark.auth
def test_login_with_missing_phone():
    client = AuthClient()

    payload = {
        "password": "some_password",
    }

    response = client.login(payload)
    assert_status_code_in(response, [400, 401, 422])


@pytest.mark.negative
@pytest.mark.auth
def test_login_with_empty_body():
    client = AuthClient()

    response = client.login({})
    assert_status_code_in(response, [400, 401, 422])


@pytest.mark.negative
@pytest.mark.auth
def test_me_with_invalid_token(invalid_token_client):
    response = invalid_token_client.get("/auth/me")
    assert_status_code_in(response, [401, 403])


@pytest.mark.negative
@pytest.mark.auth
def test_me_without_token(anonymous_client):
    response = anonymous_client.get("/auth/me")
    assert_status_code_in(response, [401, 403])