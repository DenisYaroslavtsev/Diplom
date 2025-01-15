"""
Модуль определяет 2 модели Pydantic

Модель CreateUser используется для создания нового пользователя
Модель UserResponse используется для возврата данных пользователя
"""

from pydantic import BaseModel
from datetime import date


class CreateUser(BaseModel):
    """
    Модель для создания нового пользователя

    Атрибуты:
        email (str): Электронная почта пользователя
        password (str): Пароль пользователя
    """
    email: str
    password: str


class UserResponse(BaseModel):
    """
    Модель для ответа с данными пользователя

    Атрибуты:
        username (str): Имя пользователя
        email (str): Электронная почта пользователя
        password (str): Пароль пользователя
        repeat_password (str): Повторный ввод пароля для проверки
        birth_date (date): Дата рождения пользователя
    """
    username: str
    email: str
    password: str
    repeat_password: str
    birth_date: date
