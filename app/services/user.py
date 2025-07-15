import logging

from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.models.github import GitHubUser as GitHubUserModel
from app.schemas.github_user import GitHubUser as GitHubUserSchema

logger = logging.getLogger(__name__)


def validate_and_store_github_user(user_data: dict, db: Session) -> GitHubUserModel:
    try:
        # Validate using Pydantic
        validated = GitHubUserSchema(**user_data)
    except ValidationError as e:
        msg = f"Validation failed: {e}"
        logger.error(msg)
        raise ValueError(msg)  # noqa: B904

        # Convert to DB model
    user_dict = validated.model_dump(mode="json")
    db_user = GitHubUserModel(**user_dict)

    # Save to DB
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
