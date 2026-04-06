from __future__ import annotations

from src.schemas.trip_schema import (
    ACTIVE_TRIP_RESPONSE_SCHEMA,
    SERVICE_TYPES_RESPONSE_SCHEMA,
)
from src.utils.assertions import assert_status_code
from src.utils.schema_validator import validate_schema


class TripService:
    def __init__(self, client) -> None:
        self.client = client

    def get_service_types_and_validate(self, params: dict):
        response = self.client.get("/customer/service-types", params=params)
        assert_status_code(response, 200)

        response_json = response.json()
        validate_schema(response_json, SERVICE_TYPES_RESPONSE_SCHEMA)
        return response

    def get_active_trip_and_validate(self):
        response = self.client.get("/customer/trips/active")
        assert_status_code(response, 200)

        response_json = response.json()
        validate_schema(response_json, ACTIVE_TRIP_RESPONSE_SCHEMA)
        return response