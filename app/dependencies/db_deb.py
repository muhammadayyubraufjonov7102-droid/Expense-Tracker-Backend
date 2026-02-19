from app.db.base import Sessionlocal
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated


def get_db():
    session = Sessionlocal()
    try:
        yield session
    finally:
        session.close()
        
DBDep = Annotated[Session, Depends(get_db)]