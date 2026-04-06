import pytest

from src.clients.auth_client import AuthClient
from src.services.auth_service import AuthService
from src.utils.assertions import assert_status_code_in


@pytest.mark.smoke
@pytest.mark.auth
def test_login_success(auth_client, customer_credentials):
    service = AuthService(auth_client)
    response = service.login_and_validate(customer_credentials)

    response_json = response.json()
    assert response_json["token_type"].lower() == "bearer"
    assert response_json["role"] == "CUSTOMER"
    assert response_json["user_id"] > 0
    assert response_json["expires_in"] > 0


@pytest.mark.smoke
@pytest.mark.auth
def test_get_me_success(authenticated_customer_client):
    service = AuthService(authenticated_customer_client)
    response = service.get_me_and_validate()

    response_json = response.json()
    assert response_json["id"] > 0
    assert response_json["phone_number"].startswith("+998")
    assert response_json["role"] == "CUSTOMER"
    assert response_json["status"] == "ACTIVE"


@pytest.mark.smoke
@pytest.mark.auth
def test_get_me_unauthorized():
    client = AuthClient()
    response = client.me()
    assert_status_code_in(response, [401, 403])