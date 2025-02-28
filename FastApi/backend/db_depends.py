"""
Модуль предоставляет утилиты для работы с БД

Основая роль функции - создание и управление сессиями
"""

from FastApi.backend.db import SessionLocal


def get_db():
    """
    Генератор для получения сессии БД

    После завершения работы с сессией, она автоматически закрывается
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
