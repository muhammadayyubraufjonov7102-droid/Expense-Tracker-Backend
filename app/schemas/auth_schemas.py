from pydantic import BaseModel

class SignUp(BaseModel):
    username: str
    password: str
    

class Login(BaseModel):
    username: str
    password: str
    
class LoggedInUser(BaseModel):
    user_id: int
    
class LoginResponse(BaseModel):
    access_toke: str
    
class SignUpResponse(BaseModel):
    id: int
    username: str
    