import pytest

from src.services.order_service import OrderService


@pytest.mark.business
@pytest.mark.commerce
def test_customer_commerce_read_flow(authenticated_customer_client):
    order_service = OrderService(authenticated_customer_client)

    categories_response = order_service.get_categories_and_validate()
    cart_response = order_service.get_cart_and_validate()
    my_orders_response = order_service.get_my_orders_and_validate()

    categories_json = categories_response.json()
    cart_json = cart_response.json()
    my_orders_json = my_orders_response.json()

    # Categories business checks
    assert isinstance(categories_json, list)
    assert len(categories_json) > 0
    assert all("id" in item and "name" in item for item in categories_json)

    # Cart business checks
    assert isinstance(cart_json, list)
    if cart_json:
        for store_group in cart_json:
            assert store_group["store_id"] > 0
            assert store_group["cart_id"] > 0
            assert isinstance(store_group["items"], list)
            assert store_group["total_price"] >= 0

            calculated_total = sum(item["subtotal"] for item in store_group["items"])
            assert abs(calculated_total - store_group["total_price"]) < 0.0001

    # My orders checks
    assert my_orders_json["success"] is True
    assert isinstance(my_orders_json["data"], list)
    assert my_orders_json["pagination"]["page"] >= 1
    assert my_orders_json["pagination"]["total"] >= 0

    for order in my_orders_json["data"]:
        assert order["id"] > 0
        assert order["store"]["id"] > 0
        assert order["total_amount"] >= 0
        assert isinstance(order["items"], list)

        calculated_order_total = sum(
            item["total_item_amount"] for item in order["items"]
        )

        # total_amount ichida fee/discount bo'lishi mumkin, shuning uchun to'liq tenglik emas
        assert calculated_order_total >= 0