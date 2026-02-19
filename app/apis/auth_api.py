from fastapi import APIRouter
from app.schemas.auth_schemas import SignUp, SignUpResponse

router = APIRouter()

@router.post("/signup", response_model=SignUpResponse)
def sign_up(data: SignUp ):
    pass