import os
from datetime import datetime, timedelta
import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
CACHE = {}

def generate_token(user_id: int):
    payload = {"user_id": user_id, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["user_id"]
    except Exception:
        return None

def cache_response(user_id: int, data):
    CACHE[user_id] = {"data": data, "expiry": datetime.utcnow() + timedelta(minutes=5)}

def get_cached_response(user_id: int):
    cached_data = CACHE.get(user_id)
    if cached_data and cached_data["expiry"] > datetime.utcnow():
        return cached_data["data"]
    return None