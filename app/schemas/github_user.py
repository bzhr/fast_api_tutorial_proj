from pydantic import BaseModel, EmailStr, HttpUrl


class GitHubUser(BaseModel):
    login: str
    html_url: HttpUrl
    avatar_url: HttpUrl
    name: str | None
    email: EmailStr
    location: str | None
    bio: str | None
    twitter_username: str | None
