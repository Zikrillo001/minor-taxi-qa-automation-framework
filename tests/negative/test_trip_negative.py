import pytest

from src.utils.assertions import assert_status_code_in


@pytest.mark.negative
@pytest.mark.trip
def test_service_types_is_public_endpoint(anonymous_client):
    params = {
        "latitude": 41.3111,
        "longitude": 69.2797,
        "distance_km": 5,
    }
    response = anonymous_client.get("/customer/service-types", params=params)

    assert response.status_code == 200
    data = response.json()

    assert "region" in data
    assert "services" in data


@pytest.mark.negative
@pytest.mark.trip
def test_service_types_with_invalid_token_allowed(invalid_token_client):
    params = {
        "latitude": 41.3111,
        "longitude": 69.2797,
        "distance_km": 5,
    }
    response = invalid_token_client.get("/customer/service-types", params=params)

    assert response.status_code == 200


@pytest.mark.negative
@pytest.mark.trip
def test_service_types_with_missing_params(authenticated_customer_client):
    response = authenticated_customer_client.get("/customer/service-types")
    assert_status_code_in(response, [400, 422])


@pytest.mark.negative
@pytest.mark.trip
def test_service_types_with_invalid_latitude(authenticated_customer_client):
    params = {
        "latitude": "invalid_latitude",
        "longitude": 69.2797,
        "distance_km": 5,
    }
    response = authenticated_customer_client.get("/customer/service-types", params=params)
    assert_status_code_in(response, [400, 422])


@pytest.mark.negative
@pytest.mark.trip
def test_active_trip_with_invalid_token(invalid_token_client):
    response = invalid_token_client.get("/customer/trips/active")
    assert_status_code_in(response, [401, 403])