from __future__ import annotations

from src.schemas.order_schema import (
    CART_RESPONSE_SCHEMA,
    CATEGORIES_RESPONSE_SCHEMA,
    MY_ORDERS_RESPONSE_SCHEMA,
)
from src.utils.assertions import assert_status_code
from src.utils.schema_validator import validate_schema


class OrderService:
    def __init__(self, client) -> None:
        self.client = client

    def get_categories_and_validate(self):
        response = self.client.get("/commerce/categories")
        assert_status_code(response, 200)

        response_json = response.json()
        validate_schema(response_json, CATEGORIES_RESPONSE_SCHEMA)
        return response

    def get_cart_and_validate(self):
        response = self.client.get("/commerce/cart")
        assert_status_code(response, 200)

        response_json = response.json()
        validate_schema(response_json, CART_RESPONSE_SCHEMA)
        return response

    def get_my_orders_and_validate(self):
        response = self.client.get("/commerce/orders/my")
        assert_status_code(response, 200)

        response_json = response.json()
        validate_schema(response_json, MY_ORDERS_RESPONSE_SCHEMA)
        return response