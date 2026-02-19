from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import verify_token
from app.schemas.auth_schemas import LoggedInUser
from fastapi import Depends
from typing import Annotated


def get_current_user(paylod: HTTPAuthorizationCredentials =Depends(HTTPBearer())):
    token = paylod.credentials
    paylod = verify_token(token)
    
    return LoggedInUser.model_validate(payload)


CurrentUserDep = Annotated[LoggedInUser, Depends(get_current_user)]