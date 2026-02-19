from pydantic import BaseModel

class SignUp(BaseModel):
    username: str
    password: str
    

class Login(BaseModel):
    username: str
    password: s
    
    
class SignUpResponse(BaseModel):
    id: int
    username: str
    