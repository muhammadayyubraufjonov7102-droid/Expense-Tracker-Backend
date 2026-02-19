from pydantic import BaseModel

class SignUp(BaseModel):
    username: str
    password: str
    
    
class SignUpResponse(BaseModel):
    id: int
    username: str
    