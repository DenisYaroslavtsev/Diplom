from Flask.backend.db import Base
from sqlalchemy import Integer, Column, String, Date


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True, nullable=False)
    birth_day = Column(Date)

