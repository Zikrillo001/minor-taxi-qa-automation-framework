SERVICE_TYPES_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["region", "services"],
    "properties": {
        "region": {
            "type": "object",
            "required": ["id", "name", "city"],
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "city": {"type": "string"},
            },
            "additionalProperties": True,
        },
        "services": {
            "type": "array",
            "items": {"type": "object"},
        },
    },
    "additionalProperties": True,
}

ACTIVE_TRIP_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["message", "trip"],
    "properties": {
        "message": {"type": "string"},
        "trip": {"type": ["object", "null"]},
    },
    "additionalProperties": True,
}