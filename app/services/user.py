import logging

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.models.github import GitHubUser as GitHubUserModel
from app.schemas.github_user import GitHubUser as GitHubUserSchema

logger = logging.getLogger(__name__)


def validate_and_store_github_user(user_data: dict, db: Session) -> GitHubUserModel:
    try:
        validated = GitHubUserSchema(**user_data)
    except ValidationError as e:
        msg = f"Validation failed: {e}"
        logger.error(msg)
        raise ValueError(msg)  # noqa: B904

    user_dict = validated.model_dump(mode="json")

    user = db.query(GitHubUserModel).filter_by(login=user_dict["login"]).first()
    if user:
        logger.info(f"Updating existing user: {user.login}")
        for key, value in user_dict.items():
            setattr(user, key, value)
    else:
        logger.info(f"Creating new user: {user_dict['login']}")
        user = GitHubUserModel(**user_dict)
        db.add(user)

    db.commit()
    db.refresh(user)
    return user
