from src.schemas.common_schema import PAGINATION_SCHEMA


CATEGORY_ITEM_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "slug", "is_has_child", "is_shops", "is_restaurant"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "slug": {"type": "string"},
        "image_url": {"type": ["string", "null"]},
        "is_has_child": {"type": "boolean"},
        "is_shops": {"type": "boolean"},
        "is_restaurant": {"type": "boolean"},
    },
    "additionalProperties": True,
}

CATEGORIES_RESPONSE_SCHEMA = {
    "type": "array",
    "items": CATEGORY_ITEM_SCHEMA,
}

CART_RESPONSE_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "required": [
            "store_id",
            "cart_id",
            "store_name",
            "items",
            "total_price",
        ],
        "properties": {
            "store_id": {"type": "integer"},
            "cart_id": {"type": "integer"},
            "store_name": {"type": "string"},
            "store_image": {"type": ["string", "null"]},
            "store_slug": {"type": "string"},
            "items": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": [
                        "id",
                        "product_id",
                        "name",
                        "price",
                        "quantity",
                        "subtotal",
                    ],
                    "properties": {
                        "id": {"type": "integer"},
                        "product_id": {"type": "integer"},
                        "product_slug": {"type": "string"},
                        "name": {"type": "string"},
                        "image_url": {"type": ["string", "null"]},
                        "price": {"type": "number"},
                        "quantity": {"type": "integer"},
                        "variation": {"type": ["object", "null"]},
                        "subtotal": {"type": "number"},
                    },
                    "additionalProperties": True,
                },
            },
            "total_price": {"type": "number"},
        },
        "additionalProperties": True,
    },
}

MY_ORDERS_RESPONSE_SCHEMA = {
    "type": "object",
    "required": ["success", "data", "pagination"],
    "properties": {
        "success": {"type": "boolean"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "required": [
                    "id",
                    "order_number",
                    "store",
                    "status",
                    "total_amount",
                    "payment",
                    "created_at",
                    "items",
                ],
                "properties": {
                    "id": {"type": "integer"},
                    "order_number": {"type": "string"},
                    "store": {
                        "type": "object",
                        "required": ["id", "name"],
                        "properties": {
                            "id": {"type": "integer"},
                            "name": {"type": "string"},
                        },
                        "additionalProperties": True,
                    },
                    "status": {"type": "string"},
                    "order_note": {"type": "string"},
                    "total_amount": {"type": "number"},
                    "discount_amount": {"type": "number"},
                    "service_fee": {"type": "number"},
                    "payment": {
                        "type": "object",
                        "required": ["method", "status"],
                        "properties": {
                            "method": {"type": "string"},
                            "status": {"type": "string"},
                        },
                        "additionalProperties": True,
                    },
                    "created_at": {"type": "string"},
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": [
                                "id",
                                "item_name",
                                "price_snapshot",
                                "quantity",
                                "total_item_amount",
                            ],
                            "properties": {
                                "id": {"type": "integer"},
                                "item_name": {"type": "string"},
                                "item_image_url": {"type": ["string", "null"]},
                                "price_snapshot": {"type": "number"},
                                "quantity": {"type": "integer"},
                                "total_item_amount": {"type": "number"},
                                "comment": {"type": ["string", "null"]},
                            },
                            "additionalProperties": True,
                        },
                    },
                },
                "additionalProperties": True,
            },
        },
        "pagination": PAGINATION_SCHEMA,
    },
    "additionalProperties": True,
}