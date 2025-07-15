import logging
from urllib.parse import urlencode

import requests

from app.settings import AUTHORIZE_URL, CLIENT_ID, CLIENT_SECRET, REQUESTS_TIMEOUT, TOKEN_URL, USER_API_URL

logger = logging.getLogger(__name__)


class GitHubAPI:
    def __init__(self, client_id: str, client_secret: str, timeout: float):
        self.client_id = client_id
        self.client_secret = client_secret
        self.timeout = timeout

    def get_authorization_url(self) -> str:
        params = {"client_id": self.client_id, "scope": "read:user"}
        return f"{AUTHORIZE_URL}?{urlencode(params)}"

    def exchange_code_for_token(self, code: str) -> str:
        response = requests.post(
            TOKEN_URL,
            headers={"Accept": "application/json"},
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": code,
            },
            timeout=self.timeout,
        )
        data = response.json()
        if "access_token" not in data:
            logger.error("Token error: %s", data)
            msg = "Token exchange failed"
            logger.error(msg)
            raise Exception(msg)
        return data["access_token"]

    def fetch_user(self, access_token: str) -> dict:
        response = requests.get(
            USER_API_URL,
            headers={
                "Authorization": f"token {access_token}",
                "Accept": "application/vnd.github+json",
            },
            timeout=self.timeout,
        )
        return response.json()


github = GitHubAPI(CLIENT_ID, CLIENT_SECRET, REQUESTS_TIMEOUT)
