from fastapi import Depends, HTTPException, status
from utils.cache import decode_token
from database import get_db

def authenticate_user(token: str, db = Depends(get_db)):
    user_id = decode_token(token)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return user_id