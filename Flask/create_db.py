"""
Модуль для создания Базы Данных
"""

from Flask.backend.db import engine, Base


def create_db():
    """
    Создаёт таблицу в базе данных
    """
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_db()
