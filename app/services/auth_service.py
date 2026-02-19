from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.auth_schemas import SignUp, Login
from fastapi import HTTPException
from app.core.security import hash_password, verify_password, create_accsess_token


def handle_singup(data: SignUp, db: Session):
    user = db.execute(select(User).where(User.username == data.username))
    if user:
        raise HTTPException(status_code=409, detail="Username alerady exist!")
    
    user = User(username=data.username, password=hash_password(data.password))
    
    db.add(user)
    db.commit()
    
    return user

def handle_login(data: Login, db: Session):
    user = db.execute(select(User).where(User.username == data.username))
    if not user:
        raise HTTPException(status_code=401, detail="Username or password is invalid!")
    
    if verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Username or password is invalid!")
    return {
        "access_toke": create_accsess_token(user.id)
    }
    