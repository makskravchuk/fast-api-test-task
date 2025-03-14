from fastapi import HTTPException, status
from repositories.user_repository import get_user_by_email, create_user
from schemas import UserSignup, UserLogin
from utils.cache import generate_token

def signup_user(db, user_data: UserSignup):
    if get_user_by_email(db, user_data.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    user = create_user(db, user_data.dict())
    token = generate_token(user.id)
    return {"token": token}

def login_user(db, user_data: UserLogin):
    user = get_user_by_email(db, user_data.email)
    if not user or user.password != user_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = generate_token(user.id)
    return {"token": token}