from sqlalchemy import Column, Integer, String

from app.db.base import Base


class GitHubUser(Base):
    __tablename__ = "github_users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    html_url = Column(String)
    avatar_url = Column(String)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    location = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    twitter_username = Column(String, nullable=True)
