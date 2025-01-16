"""
Модуль создаёт модель User для работы с таблицей users в базе данных
Каждый атрибут модели соответствует столбцу в таблице, с указанием типа данных и дополнительных параметров
"""

from Flask.backend.db import Base
from sqlalchemy import Integer, Column, String, Date


class User(Base):
    """
    Модель пользователя для базы данных
    Атрибуты:
        __tablename__ (str): Название таблицы в базе данных
        id (int): Уникальный идентификатор пользователя (первичный ключ)
        username (str): Уникальное имя пользователя
        password (str): Пароль пользователя
        email (str): Уникальный email(эл. почта) пользователя
        birth_day (date): Дата рождения пользователя
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True, nullable=False)
    birth_day = Column(Date)
