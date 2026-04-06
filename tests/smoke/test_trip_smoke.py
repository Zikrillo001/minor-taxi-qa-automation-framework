import pytest

from src.clients.base_client import BaseClient


@pytest.mark.smoke
@pytest.mark.trip
def test_get_service_types_requires_auth(customer_access_token):
    client = BaseClient(token=customer_access_token)

    params = {
        "latitude": 41.3111,
        "longitude": 69.2797,
        "distance_km": 5,
    }
    response = client.get("/customer/service-types", params=params)

    assert response.status_code in [200, 204], (
        f"Expected 200/204, got {response.status_code}. Response: {response.text}"
    )


@pytest.mark.smoke
@pytest.mark.trip
def test_get_active_trip(authenticated_customer_client):
    response = authenticated_customer_client.get("/customer/trips/active")
    assert response.status_code in [200, 204], (
        f"Expected 200/204, got {response.status_code}. Response: {response.text}"
    )