from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app.services.github_oauth import (
    exchange_code_for_token,
    fetch_github_user,
    get_github_authorization_url,
)

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user = request.session.get("user")
    if user:
        return f"<h1>Welcome, {user['login']}</h1><pre>{user}</pre>"
    return '<a href="/login">Login with GitHub</a>'


@router.get("/login")
async def login():
    return RedirectResponse(get_github_authorization_url())


@router.get("/callback")
async def callback(request: Request, code: str = None):
    if not code:
        raise HTTPException(status_code=400, detail="Missing code")

    access_token = exchange_code_for_token(code)
    user_data = fetch_github_user(access_token)
    request.session["user"] = user_data
    return RedirectResponse("/")


@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/")
