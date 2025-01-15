from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = 'sqlite:///users.db'
engine = create_engine(DATABASE_URL)


def get_db():
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


class Base(DeclarativeBase):
    pass
