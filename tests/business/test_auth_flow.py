import pytest

from src.services.auth_service import AuthService
from src.services.business_flow_service import BusinessFlowService


@pytest.mark.business
@pytest.mark.auth
def test_customer_auth_flow(auth_client, authenticated_customer_client, customer_credentials):
    login_auth_service = AuthService(auth_client)
    me_auth_service = AuthService(authenticated_customer_client)

    flow_service = BusinessFlowService(
        auth_service=None,
        order_service=None,
        trip_service=None,
    )

    login_response = login_auth_service.login_and_validate(customer_credentials)
    me_response = me_auth_service.get_me_and_validate()

    login_json = login_response.json()
    me_json = me_response.json()

    assert login_json["role"] == "CUSTOMER"
    assert me_json["role"] == "CUSTOMER"
    assert login_json["user_id"] == me_json["id"]
    assert me_json["phone_number"] == customer_credentials["phone_number"]
    assert me_json["status"] == "ACTIVE"