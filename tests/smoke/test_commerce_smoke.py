import pytest

from src.clients.base_client import BaseClient


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_categories():
    client = BaseClient()
    response = client.get("/commerce/categories")

    assert response.status_code == 200, (
        f"Expected 200, got {response.status_code}. Response: {response.text}"
    )


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_cart_authenticated(authenticated_customer_client):
    response = authenticated_customer_client.get("/commerce/cart")
    assert response.status_code == 200, (
        f"Expected 200, got {response.status_code}. Response: {response.text}"
    )


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_my_orders_authenticated(authenticated_customer_client):
    response = authenticated_customer_client.get("/commerce/orders/my")
    assert response.status_code == 200, (
        f"Expected 200, got {response.status_code}. Response: {response.text}"
    )