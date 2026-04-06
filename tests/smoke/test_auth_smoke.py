import pytest

from src.clients.auth_client import AuthClient
from src.utils.assertions import assert_status_code, assert_status_code_in, pretty_json


@pytest.mark.smoke
@pytest.mark.auth
def test_login_success(customer_login_response):
    assert_status_code(customer_login_response, 200)

    response_json = customer_login_response.json()
    assert isinstance(response_json, dict), "Login response is not a JSON object"

    possible_keys = ["access_token", "refresh_token", "token", "access"]
    found = any(key in response_json for key in possible_keys)

    assert found, f"Token keys not found in response:\n{pretty_json(response_json)}"


@pytest.mark.smoke
@pytest.mark.auth
def test_get_me_success(authenticated_customer_client):
    response = authenticated_customer_client.me()
    assert_status_code(response, 200)

    response_json = response.json()
    assert isinstance(response_json, dict), "Me response is not a JSON object"

    expected_any_of = ["id", "phone_number", "full_name", "role"]
    found = [key for key in expected_any_of if key in response_json]

    assert found, f"No expected user fields found:\n{pretty_json(response_json)}"


@pytest.mark.smoke
@pytest.mark.auth
def test_get_me_unauthorized():
    client = AuthClient()
    response = client.me()
    assert_status_code_in(response, [401, 403])