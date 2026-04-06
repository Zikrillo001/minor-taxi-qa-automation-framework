from __future__ import annotations

import json
from typing import Any


def pretty_json(data: Any) -> str:
    try:
        return json.dumps(data, indent=2, ensure_ascii=False)
    except TypeError:
        return str(data)


def get_response_debug_message(response) -> str:
    try:
        body = response.json()
    except Exception:
        body = response.text

    return (
        f"\nStatus: {response.status_code}"
        f"\nHeaders: {dict(response.headers)}"
        f"\nBody: {pretty_json(body)}"
    )


def assert_status_code(response, expected: int) -> None:
    assert response.status_code == expected, (
        f"Expected status {expected}, but got {response.status_code}."
        f"{get_response_debug_message(response)}"
    )


def assert_status_code_in(response, expected_statuses: list[int]) -> None:
    assert response.status_code in expected_statuses, (
        f"Expected one of {expected_statuses}, but got {response.status_code}."
        f"{get_response_debug_message(response)}"
    )


def assert_json_has_keys(data: dict[str, Any], required_keys: list[str]) -> None:
    missing_keys = [key for key in required_keys if key not in data]
    assert not missing_keys, (
        f"Missing keys in response JSON: {missing_keys}\n"
        f"Actual JSON:\n{pretty_json(data)}"
    )