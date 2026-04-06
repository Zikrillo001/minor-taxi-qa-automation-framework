import pytest

from src.services.trip_service import TripService


@pytest.mark.business
@pytest.mark.trip
def test_customer_trip_read_flow(authenticated_customer_client):
    trip_service = TripService(authenticated_customer_client)

    params = {
        "latitude": 41.3111,
        "longitude": 69.2797,
        "distance_km": 5,
    }

    service_types_response = trip_service.get_service_types_and_validate(params)
    active_trip_response = trip_service.get_active_trip_and_validate()

    service_types_json = service_types_response.json()
    active_trip_json = active_trip_response.json()

    # Service types checks
    assert "region" in service_types_json
    assert "services" in service_types_json
    assert service_types_json["region"]["id"] > 0
    assert service_types_json["region"]["name"]
    assert service_types_json["region"]["city"]

    assert isinstance(service_types_json["services"], list)

    for service in service_types_json["services"]:
        assert "id" in service
        assert "name" in service

    # Active trip checks
    assert "message" in active_trip_json
    assert "trip" in active_trip_json

    if active_trip_json["trip"] is None:
        assert active_trip_json["message"]
    else:
        assert isinstance(active_trip_json["trip"], dict)