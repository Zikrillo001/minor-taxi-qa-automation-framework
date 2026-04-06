from __future__ import annotations

import json
from typing import Any


def assert_status_code(actual: int, expected: int) -> None:
    assert actual == expected, f"Expected status {expected}, but got {actual}"


def assert_json_has_keys(data: dict[str, Any], required_keys: list[str]) -> None:
    missing_keys = [key for key in required_keys if key not in data]
    assert not missing_keys, f"Missing keys in response JSON: {missing_keys}"


def pretty_json(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)