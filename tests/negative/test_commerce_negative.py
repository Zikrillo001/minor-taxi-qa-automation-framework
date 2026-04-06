import pytest

from src.utils.assertions import assert_status_code_in


@pytest.mark.negative
@pytest.mark.commerce
def test_cart_without_token(anonymous_client):
    response = anonymous_client.get("/commerce/cart")
    assert_status_code_in(response, [401, 403])


@pytest.mark.negative
@pytest.mark.commerce
def test_my_orders_without_token(anonymous_client):
    response = anonymous_client.get("/commerce/orders/my")
    assert_status_code_in(response, [401, 403])


@pytest.mark.negative
@pytest.mark.commerce
def test_cart_with_invalid_token(invalid_token_client):
    response = invalid_token_client.get("/commerce/cart")
    assert_status_code_in(response, [401, 403])


@pytest.mark.negative
@pytest.mark.commerce
def test_order_detail_with_invalid_id(authenticated_customer_client):
    response = authenticated_customer_client.get("/commerce/orders/999999999")
    assert_status_code_in(response, [404, 422])


@pytest.mark.negative
@pytest.mark.commerce
def test_categories_with_invalid_query_param():
    from src.clients.base_client import BaseClient

    client = BaseClient()
    response = client.get("/commerce/categories", params={"page": "invalid"})
    assert response.status_code in [200, 400, 422], (
        f"Unexpected status code: {response.status_code}, body: {response.text}"
    )