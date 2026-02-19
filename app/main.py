from fastapi import FastAPI
from app.apis import auth_api, me_api, expense_api

app = FastAPI()

app.include_router(auth_api.router)
app.include_router(me_api.router)
app.include_router(expense_api.router)