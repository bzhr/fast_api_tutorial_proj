from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.db.base import Base
from app.db.session import engine
from app.logging_config import setup_logging
from app.models import *  # noqa: F401, F403
from app.routes.github_auth import router as github_router
from app.settings import SESSION_SECRET

setup_logging()

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set a consistent secret key (don't use os.urandom() every time or the session resets on reload)
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

app.include_router(github_router, prefix="", tags=["GitHub OAuth"])
