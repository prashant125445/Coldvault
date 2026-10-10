from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate
from app.core.security import hash_password, verify_password


def create_user(db: Session, user_data: UserCreate):

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    # Hash password
    hashed_password = hash_password(
        user_data.password
    )

    # Create user
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        name_of_cold_storage=user_data.name_of_cold_storage,
        password=hashed_password,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    # Find user
    user = db.query(User).filter(
        User.email == email
    ).first()

    # User doesn't exist
    if not user:
        return None

    # Check password
    if not verify_password(
        password,
        user.password
    ):
        return None

    # Check active status
    if not user.is_active:
        return None

    return user