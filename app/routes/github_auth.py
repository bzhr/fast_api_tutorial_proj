import logging

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.github import GitHubUser
from app.services.github_oauth import github
from app.services.user import validate_and_store_github_user

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user = request.session.get("user")
    if user:
        return f"""
        <html>
            <head><title>Welcome</title></head>
            <body>
                <h1>Welcome, {user["login"]}</h1>
                <p><a href="/user/{user["login"]}">Go to your profile</a></p>
                <form action="/logout" method="get">
                    <button type="submit">Logout</button>
                </form>
            </body>
        </html>
        """
    return '<a href="/login">Login with GitHub</a>'


@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=302)


@router.get("/login")
async def login():
    return RedirectResponse(github.get_authorization_url())


@router.get("/callback")
async def callback(request: Request, code: str = None, db: Session = Depends(get_db)):  # noqa: B008
    if not code:
        logger.error("Missing code in oauth callback request")
        raise HTTPException(status_code=400, detail="Missing code")

    access_token = github.exchange_code_for_token(code)
    user_data = github.fetch_user(access_token)
    user = validate_and_store_github_user(user_data, db)
    request.session["user"] = user_data
    return RedirectResponse(url=f"/user/{user.login}", status_code=302)


@router.get("/user/{login}", response_class=HTMLResponse)
def get_user_profile(login: str, db: Session = Depends(get_db)):  # noqa: B008
    user = db.query(GitHubUser).filter(GitHubUser.login == login).first()
    if not user:
        logger.error(f"User with login {login} not found")
        raise HTTPException(status_code=404, detail="User not found")

    return f"""
    <html>
        <head>
            <title>{user.name or user.login}'s Profile</title>
        </head>
        <body style="font-family: sans-serif; max-width: 600px; margin: auto;">
            <h1>{user.name or user.login}</h1>
            <img src="{user.avatar_url}" alt="Avatar" width="150" style="border-radius: 8px;" />
            <p><strong>Login:</strong> {user.login}</p>
            <p><strong>Bio:</strong> {user.bio or "No bio available"}</p>
            <p><strong>Location:</strong> {user.location or "Unknown"}</p>
            <p><strong>GitHub:</strong> <a href="{user.html_url}" target="_blank">{user.html_url}</a></p>
            <p><strong>Twitter:</strong> {user.twitter_username or "—"}</p>
        </body>
    </html>
    """
