import logging
from urllib.parse import urlencode

import requests

from app.settings import AUTHORIZE_URL, CLIENT_ID, CLIENT_SECRET, REQUESTS_TIMEOUT, TOKEN_URL, USER_API_URL

logger = logging.getLogger(__name__)


def get_github_authorization_url():
    params = {
        "client_id": CLIENT_ID,
        "scope": "read:user",
    }
    return f"{AUTHORIZE_URL}?{urlencode(params)}"


def exchange_code_for_token(code: str) -> str:
    response = requests.post(
        TOKEN_URL,
        headers={"Accept": "application/json"},
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
        },
        timeout=REQUESTS_TIMEOUT,
    )
    data = response.json()
    if "access_token" not in data:
        msg = f"Token error: {data}"
        logger.error(msg)
        raise Exception(msg)
    return data["access_token"]


def fetch_github_user(access_token: str) -> dict:
    response = requests.get(
        USER_API_URL,
        headers={
            "Authorization": f"token {access_token}",
            "Accept": "application/vnd.github+json",
        },
        timeout=REQUESTS_TIMEOUT,
    )
    return response.json()
