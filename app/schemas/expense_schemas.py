from pydantic import BaseModel
from datetime import datetime


class ExpenseCreate(BaseModel):
    title: str
    
    
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: datetime
    user_id: int
    
    
    
    
