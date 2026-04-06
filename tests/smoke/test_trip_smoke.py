import pytest

from src.clients.base_client import BaseClient
from src.utils.assertions import assert_status_code_in


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
    assert_status_code_in(response, [200, 204])


@pytest.mark.smoke
@pytest.mark.trip
def test_get_active_trip(authenticated_customer_client):
    response = authenticated_customer_client.get("/customer/trips/active")
    assert_status_code_in(response, [200, 204, 404])