from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.users import (
    UserCreate,
    UserLogin,
    UserResponse
)
from app.core.database import get_db
from app.core.security import create_access_token, get_current_user
from app.models.users import User
from app.schemas.users import UserCreate, UserResponse
from app.service.users_service import (
    create_user,
    authenticate_user
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# -----------------------------
# Register Manager
# -----------------------------

@router.post("/register", response_model=UserResponse)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
   
    user = create_user(
        db,
        user_data
    )

    if  not  user:
        raise HTTPException(
            status_code=400,
             detail="Email already registered"
        )

    return user


@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user

# -----------------------------
# Login Manager
# -----------------------------

@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        user_data.email,
        user_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Create JWT
    access_token = create_access_token({
        "sub": str(user.id)
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }