from fastapi import APIRouter
from app.schemas.expense_schemas import ExpenseCreate, ExpenseResponse
from app.dependencies import DBDep, CurrentUserDep
from app.services import expense_service



router = APIRouter()


@router.post('/expenses', response_model=ExpenseResponse)
def create_exp(data: ExpenseCreate, current_user:CurrentUserDep, db: DBDep):
    return expense_service.handle_exp_create(data, current_user, db)



@router.get('/expenses', response_model=list[ExpenseResponse])
def read_exp(current_user:CurrentUserDep, db: DBDep):
    return expense_service.handle_get_all( current_user, db)


@router.put('/expenses/{expense_id}', response_class=ExpenseResponse)
def update_exp(expense_id: int,data: ExpenseCreate, current_user:CurrentUserDep, db: DBDep):
    return expense_service.handle_update(expense_id, data, current_user, db)


@router.delete('/expenses/{expense_id}', response_class=ExpenseResponse)
def delete_exp(expense_id: int, current_user:CurrentUserDep, db: DBDep):
    return expense_service.handle_delete(expense_id, current_user, db)

