"""
Модуль для работы с баззой данных SQLite с использованием SQLAlchemy

Код создаёт движок для подключения к базе данных и настраивает ссесию для взаимодействия с ней
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = 'sqlite:///users.db'
engine = create_engine(DATABASE_URL)


def get_db():
    """
    Генератор для получения сессии БД
    """
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей данных

    Наследуется от DeclarativeBase
    """
    pass
