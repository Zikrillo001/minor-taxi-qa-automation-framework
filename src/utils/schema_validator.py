from __future__ import annotations

from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_schema(data: dict | list, schema: dict) -> None:
    try:
        validate(instance=data, schema=schema)
    except ValidationError as exc:
        raise AssertionError(f"Schema validation failed: {exc.message}") from exc