from fastapi import APIRouter, Depends
from app.schemas.auth_schemas import *
from app.services import auth_service
from app.dependencies import DBDep

router = APIRouter()

@router.post("/signup", response_model=SignUpResponse)
def sign_up(data: SignUp, db: DBDep ):
    return auth_service.handle_singup(data, db)

@router.post("/login", response_model=LoginResponse)
def login_up(data: Login, db = DBDep ):
    return auth_service.handle_login(data, db)