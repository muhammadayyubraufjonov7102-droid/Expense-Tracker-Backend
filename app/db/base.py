from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session
from app.core.config import settings


class Base(DeclarativeBase):
    pass

engine = create_engine(settings.DB_URL)

Sessionlocal = Session(bind=engine)