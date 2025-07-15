from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.routes.github_auth import router as github_router
from app.settings import SESSION_SECRET

app = FastAPI()

# Set a consistent secret key (don't use os.urandom() every time or the session resets on reload)
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET)

app.include_router(github_router, prefix="", tags=["GitHub OAuth"])
