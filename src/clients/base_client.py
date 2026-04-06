from __future__ import annotations

from typing import Any

import requests

from src.utils.config_reader import get_api_prefix, get_base_url, get_timeout
from src.utils.logger import get_logger


class BaseClient:
    def __init__(self, token: str | None = None) -> None:
        self.base_url = get_base_url()
        self.api_prefix = get_api_prefix()
        self.timeout = get_timeout()
        self.logger = get_logger(self.__class__.__name__)
        self.session = requests.Session()

        self.default_headers = {
            "Accept": "application/json",
        }

        if token:
            self.default_headers["Authorization"] = f"Bearer {token}"

    def _build_url(self, endpoint: str) -> str:
        endpoint = endpoint if endpoint.startswith("/") else f"/{endpoint}"
        return f"{self.base_url}{self.api_prefix}{endpoint}"

    def _log_request(self, method: str, url: str, **kwargs: Any) -> None:
        self.logger.info("REQUEST %s %s", method.upper(), url)

        headers = kwargs.get("headers")
        params = kwargs.get("params")
        json_body = kwargs.get("json")
        data = kwargs.get("data")

        if headers:
            self.logger.info("Request headers: %s", headers)
        if params:
            self.logger.info("Request params: %s", params)
        if json_body is not None:
            self.logger.info("Request json: %s", json_body)
        if data is not None:
            self.logger.info("Request data: %s", data)

    def _log_response(self, response: requests.Response) -> None:
        self.logger.info("RESPONSE status=%s", response.status_code)

        try:
            body = response.json()
        except Exception:
            body = response.text

        self.logger.info("Response body: %s", body)

    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ) -> requests.Response:
        url = self._build_url(endpoint)

        custom_headers = kwargs.pop("headers", {})
        merged_headers = {**self.default_headers, **custom_headers}

        request_kwargs = {
            "headers": merged_headers,
            "timeout": self.timeout,
            **kwargs,
        }

        self._log_request(method, url, **request_kwargs)

        response = self.session.request(
            method=method.upper(),
            url=url,
            **request_kwargs,
        )

        self._log_response(response)
        return response

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("PUT", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)