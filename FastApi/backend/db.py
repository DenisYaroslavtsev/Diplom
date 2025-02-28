"""
Модуль для работы с баззой данных SQLite с использованием SQLAlchemy

Код создаёт движок для подключения к базе данных и настраивает ссесию для взаимодействия с ней
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///database.db', echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей данных

    Наследуется от DeclarativeBase
    """
    pass
