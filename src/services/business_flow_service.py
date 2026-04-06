from __future__ import annotations


class BusinessFlowService:
    def __init__(self, auth_service, order_service, trip_service) -> None:
        self.auth_service = auth_service
        self.order_service = order_service
        self.trip_service = trip_service

    def execute_auth_flow(self, credentials: dict) -> dict:
        login_response = self.auth_service.login_and_validate(credentials)
        me_response = self.auth_service.get_me_and_validate()

        return {
            "login": login_response.json(),
            "me": me_response.json(),
        }

    def execute_commerce_read_flow(self) -> dict:
        categories_response = self.order_service.get_categories_and_validate()
        cart_response = self.order_service.get_cart_and_validate()
        my_orders_response = self.order_service.get_my_orders_and_validate()

        return {
            "categories": categories_response.json(),
            "cart": cart_response.json(),
            "my_orders": my_orders_response.json(),
        }

    def execute_trip_read_flow(self, params: dict) -> dict:
        service_types_response = self.trip_service.get_service_types_and_validate(params)
        active_trip_response = self.trip_service.get_active_trip_and_validate()

        return {
            "service_types": service_types_response.json(),
            "active_trip": active_trip_response.json(),
        }