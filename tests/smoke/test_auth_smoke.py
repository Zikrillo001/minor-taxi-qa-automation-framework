import pytest

from src.utils.assertions import assert_json_has_keys, assert_status_code, pretty_json


@pytest.mark.smoke
@pytest.mark.auth
def test_login_success(customer_login_response):
    assert_status_code(customer_login_response.status_code, 200)

    response_json = customer_login_response.json()
    assert isinstance(response_json, dict), "Login response is not a JSON object"

    # TokenResponse fieldlari real API responsega qarab keyin aniqlashtiriladi
    possible_keys = ["access_token", "refresh_token", "token", "access"]
    found = any(key in response_json for key in possible_keys)

    assert found, f"Token keys not found in response:\n{pretty_json(response_json)}"


@pytest.mark.smoke
@pytest.mark.auth
def test_get_me_success(authenticated_customer_client):
    response = authenticated_customer_client.me()
    assert_status_code(response.status_code, 200)

    response_json = response.json()
    assert isinstance(response_json, dict), "Me response is not a JSON object"

    # Minimal profile checks
    expected_any_of = ["id", "phone_number", "full_name", "role"]
    found = [key for key in expected_any_of if key in response_json]

    assert found, f"No expected user fields found:\n{pretty_json(response_json)}"


@pytest.mark.smoke
@pytest.mark.auth
def test_get_me_unauthorized():
    client = __import__("src.clients.auth_client", fromlist=["AuthClient"]).AuthClient()
    response = client.me()

    assert response.status_code in [401, 403], (
        f"Expected 401 or 403 for unauthorized request, got {response.status_code}"
    )