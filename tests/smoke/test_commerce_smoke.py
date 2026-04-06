import pytest

from src.clients.base_client import BaseClient
from src.utils.assertions import assert_status_code, assert_status_code_in


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_categories():
    client = BaseClient()
    response = client.get("/commerce/categories")
    assert_status_code(response, 200)


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_cart_authenticated(authenticated_customer_client):
    response = authenticated_customer_client.get("/commerce/cart")
    assert_status_code(response, 200)


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_my_orders_authenticated(authenticated_customer_client):
    response = authenticated_customer_client.get("/commerce/orders/my")
    assert_status_code_in(response, [200, 204])