from __future__ import annotations

from requests import Response

from src.clients.base_client import BaseClient


class AuthClient(BaseClient):
    def login(self, payload: dict) -> Response:
        return self.post("/auth/login", json=payload)

    def login_with_phone(self, phone_number: str, password: str) -> Response:
        payload = {
            "phone_number": phone_number,
            "password": password,
        }
        return self.login(payload)

    def login_with_phone_alt(self, phone: str, password: str) -> Response:
        payload = {
            "phone": phone,
            "password": password,
        }
        return self.login(payload)

    def login_with_username(self, username: str, password: str) -> Response:
        payload = {
            "username": username,
            "password": password,
        }
        return self.login(payload)

    def login_with_email(self, email: str, password: str) -> Response:
        payload = {
            "email": email,
            "password": password,
        }
        return self.login(payload)

    def me(self) -> Response:
        return self.get("/auth/me")

    def refresh(self, refresh_token: str) -> Response:
        payload = {"refresh_token": refresh_token}
        return self.post("/auth/refresh", json=payload)

    def logout(self) -> Response:
        return self.post("/auth/logout")