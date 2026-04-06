from __future__ import annotations

from requests import Response

from src.clients.base_client import BaseClient


class AuthClient(BaseClient):
    def login(self, payload: dict) -> Response:
        return self.post("/auth/login", json=payload)

    def me(self) -> Response:
        return self.get("/auth/me")

    def refresh(self, refresh_token: str) -> Response:
        payload = {"refresh_token": refresh_token}
        return self.post("/auth/refresh", json=payload)

    def logout(self) -> Response:
        return self.post("/auth/logout")