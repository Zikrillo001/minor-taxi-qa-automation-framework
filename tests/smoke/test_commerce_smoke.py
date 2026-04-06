import pytest

from src.clients.base_client import BaseClient
from src.services.order_service import OrderService


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_categories():
    service = OrderService(BaseClient())
    response = service.get_categories_and_validate()

    response_json = response.json()
    assert len(response_json) > 0
    assert all("id" in item for item in response_json)
    assert any(item["is_restaurant"] or item["is_shops"] for item in response_json)


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_cart_authenticated(authenticated_customer_client):
    service = OrderService(authenticated_customer_client)
    response = service.get_cart_and_validate()

    response_json = response.json()
    assert isinstance(response_json, list)

    if response_json:
        first_store = response_json[0]
        assert first_store["store_id"] > 0
        assert first_store["cart_id"] > 0
        assert first_store["total_price"] >= 0


@pytest.mark.smoke
@pytest.mark.commerce
def test_get_my_orders_authenticated(authenticated_customer_client):
    service = OrderService(authenticated_customer_client)
    response = service.get_my_orders_and_validate()

    response_json = response.json()
    assert response_json["success"] is True
    assert "pagination" in response_json
    assert response_json["pagination"]["page"] >= 1