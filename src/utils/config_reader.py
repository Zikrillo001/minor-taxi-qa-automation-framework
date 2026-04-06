import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"

# override=False qoldiramiz, shell env bo'lsa shuni ishlatadi
load_dotenv(dotenv_path=ENV_PATH)


def get_env(name: str, default: str | None = None, required: bool = False) -> str | None:
    value = os.getenv(name, default)

    if required and (value is None or str(value).strip() == ""):
        raise ValueError(
            f"Required environment variable '{name}' is missing. "
            f"Expected .env at: {ENV_PATH}"
        )
    return value


def get_base_url() -> str:
    return str(get_env("BASE_URL", required=True)).rstrip("/")


def get_api_prefix() -> str:
    return str(get_env("API_PREFIX", "/api/v1"))


def get_timeout() -> int:
    return int(str(get_env("TIMEOUT", "20")))


def get_customer_credentials() -> dict:
    return {
        "phone_number": str(get_env("CUSTOMER_PHONE", "")).strip(),
        "password": str(get_env("CUSTOMER_PASSWORD", "")).strip(),
    }


def get_seller_credentials() -> dict:
    return {
        "phone_number": str(get_env("SELLER_PHONE", "")).strip(),
        "password": str(get_env("SELLER_PASSWORD", "")).strip(),
    }


def get_admin_credentials() -> dict:
    return {
        "phone_number": str(get_env("ADMIN_PHONE", "")).strip(),
        "password": str(get_env("ADMIN_PASSWORD", "")).strip(),
    }


def debug_env_info() -> dict:
    return {
        "base_dir": str(BASE_DIR),
        "env_path": str(ENV_PATH),
        "env_exists": ENV_PATH.exists(),
        "base_url_present": bool(os.getenv("BASE_URL")),
        "api_prefix": os.getenv("API_PREFIX"),
    }