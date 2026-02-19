from passlib.hash import pbkdf2_sha256
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.core.config import settings
from fastapi import HTTPException

def hash_password(plain_password):
    return pbkdf2_sha256.hash(plain_password)



def verify_password(plain_password, hashed_password):
    return pbkdf2_sha256.verify(plain_password, hashed_password)

def create_accsess_token(user_id):
    to_encode = {
        "user_id": user_id,
        "exp": datetime.now(timezone) + timedelta(minutes=30)
    }
    
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.JWT_ALGO)

def verify_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGO)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid!")
    