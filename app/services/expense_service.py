from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import Expense
from app.schemas.expense_schemas import ExpenseCreate
from app.schemas.auth_schemas import LoggedInUser
from fastapi import HTTPException


def handle_exp_create(data: ExpenseCreate, current_user:LoggedInUser, db:Session):
    expense = Expense(**data.model_dump(), user_id=current_user.user_id)
    
    db.add(expense)
    
    db.commit()
    
    return expense

def handle_get_all(current_user:LoggedInUser, db:Session):
    return db.execute(select(Expense).where(Expense.user_id==current_user.user_id)).scalars().all()


def handle_update(expense_id: int, data: ExpenseCreate, current_user:LoggedInUser, db:Session): 
    expense = db.execute(select(Expense).where(Expense.id==expense_id, Expense.user_id==current_user.user_id)).scalar_one_or_none()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense is not found!")
        
    for key, value in data.model_dump().item():
        setattr(expense, key, value)
        
    db.add()
    db.refresh(expense)
    return expense

def handle_delete(expense_id: int, data: ExpenseCreate, current_user:LoggedInUser, db:Session): 
    expense = db.execute(select(Expense).where(Expense.id==expense_id, Expense.user_id==current_user.user_id)).scalar_one_or_none()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense is not found!")
           
    db.delete(expense)
    db.commit()
    return "detail: Expense is deleted!"
