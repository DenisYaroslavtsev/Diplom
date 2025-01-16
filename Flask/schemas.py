"""
Модуль определяет 2 модели Pydantic

Модель CreateUser используется для создания нового пользователя
Модель UserResponse используется для возврата данных пользователя
"""

from pydantic import EmailStr, BaseModel
from datetime import date


class UserResponse(BaseModel):
    """
    Модель для регистрации пользователя

    Атрибуты:
        username (str): Имя пользователя
        email (Emailstr): Электронная почта пользователя
        password (str): Пароль пользователя
        repeat_password (str): Повторный ввод пароля для проверки
        birth_date (date): Дата рождения пользователя
    """
    username: str
    password: str
    repeat_password: str
    email: EmailStr
    birth_date: date


class CreateUser(BaseModel):
    """
    Модель для входа пользователя

    Атрибуты:
        email (emailstr): Электронная почта пользователя
        password (str): Пароль пользователя
    """
    email: EmailStr
    password: str
