from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db import Expense
from app.schemas.expense_schemas import ExpenseCreate
from app.schemas.auth_schemas import LoggedInUser

def handle_exp_create(data: ExpenseCreate, current_user:LoggedInUser, db:Session):
    expense = Expense(**data.model_dump(), user_id=current_user.user_id)
    
    db.add(expense)
    
    db.commit()
    
    return expense

def handle_get_all(current_user:LoggedInUser, db:Session):
    return db.execute(select(Expense).where(Expense.user_id==current_user.user_id)).scalars().all()