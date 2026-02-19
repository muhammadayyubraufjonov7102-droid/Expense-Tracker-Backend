from fastapi import APIRouter
from app.schemas.expense_schemas import ExpenseCreate, ExpenseResponse
from app.dependencies import DBDep, CurrentUserDep
from app.services import expense_service



router = APIRouter


@router.post('/expenses', response_model=ExpenseResponse)
def create_exp(data: ExpenseCreate, current_user:CurrentUserDep, db: DBDep):
    return expense_service.handle_exp_create(data, current_user, db)



@router.post('/expenses', response_model=list[ExpenseResponse])
def create_exp(current_user:CurrentUserDep, db: DBDep):
    return expense_service.handle_get_all( current_user, db)
