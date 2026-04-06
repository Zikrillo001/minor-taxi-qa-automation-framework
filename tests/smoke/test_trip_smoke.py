import pytest

from src.clients.base_client import BaseClient
from src.services.trip_service import TripService


@pytest.mark.smoke
@pytest.mark.trip
def test_get_service_types_requires_auth(customer_access_token):
    client = BaseClient(token=customer_access_token)
    service = TripService(client)

    params = {
        "latitude": 41.3111,
        "longitude": 69.2797,
        "distance_km": 5,
    }
    response = service.get_service_types_and_validate(params)

    response_json = response.json()
    assert response_json["region"]["id"] > 0
    assert response_json["region"]["name"]
    assert isinstance(response_json["services"], list)


@pytest.mark.smoke
@pytest.mark.trip
def test_get_active_trip(authenticated_customer_client):
    service = TripService(authenticated_customer_client)
    response = service.get_active_trip_and_validate()

    response_json = response.json()
    assert "message" in response_json
    assert "trip" in response_json