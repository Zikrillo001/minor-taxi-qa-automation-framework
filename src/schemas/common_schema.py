PAGINATION_SCHEMA = {
    "type": "object",
    "required": ["page", "limit", "total", "total_pages"],
    "properties": {
        "page": {"type": "integer"},
        "limit": {"type": "integer"},
        "total": {"type": "integer"},
        "total_pages": {"type": "integer"},
    },
    "additionalProperties": True,
}