import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)


def get_env(name: str, default: str | None = None, required: bool = False) -> str | None:
    value = os.getenv(name, default)
    if required and not value:
        raise ValueError(f"Required environment variable '{name}' is missing.")
    return value


def get_base_url() -> str:
    return get_env("BASE_URL", required=True).rstrip("/")


def get_api_prefix() -> str:
    return get_env("API_PREFIX", "/api/v1")


def get_timeout() -> int:
    return int(get_env("TIMEOUT", "20"))


def get_customer_credentials() -> dict:
    return {
        "phone_number": get_env("CUSTOMER_PHONE", ""),
        "password": get_env("CUSTOMER_PASSWORD", ""),
    }


def get_seller_credentials() -> dict:
    return {
        "phone_number": get_env("SELLER_PHONE", ""),
        "password": get_env("SELLER_PASSWORD", ""),
    }


def get_admin_credentials() -> dict:
    return {
        "phone_number": get_env("ADMIN_PHONE", ""),
        "password": get_env("ADMIN_PASSWORD", ""),
    }