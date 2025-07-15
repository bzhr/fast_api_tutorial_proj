import os

from dotenv import load_dotenv

load_dotenv()

SESSION_SECRET = os.getenv("SESSION_SECRET")

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

AUTHORIZE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
USER_API_URL = "https://api.github.com/user"

REQUESTS_TIMEOUT = 10  # seconds
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
