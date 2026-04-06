import pytest

from src.utils.assertions import assert_status_code_in


@pytest.mark.security
@pytest.mark.admin
def test_customer_cannot_access_admin_drivers(authenticated_customer_client):
    response = authenticated_customer_client.get("/admin/drivers")
    assert_status_code_in(response, [401, 403])


@pytest.mark.security
@pytest.mark.admin
def test_customer_cannot_access_admin_payment_analytics(authenticated_customer_client):
    response = authenticated_customer_client.get("/admin/payment-analytics")
    assert_status_code_in(response, [401, 403, 422])


@pytest.mark.security
@pytest.mark.admin
def test_customer_cannot_access_admin_orders(authenticated_customer_client):
    response = authenticated_customer_client.get("/admin/orders")
    assert_status_code_in(response, [401, 403])


@pytest.mark.security
@pytest.mark.trip
def test_anonymous_user_cannot_access_active_trip(anonymous_client):
    response = anonymous_client.get("/customer/trips/active")
    assert_status_code_in(response, [401, 403])


@pytest.mark.security
@pytest.mark.commerce
def test_anonymous_user_cannot_access_my_orders(anonymous_client):
    response = anonymous_client.get("/commerce/orders/my")
    assert_status_code_in(response, [401, 403])