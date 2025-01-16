"""
Модуль для определения модели пользователя
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Модель пользователя, расширяющая стандартную модель пользователя Django

    Добавляет поле для хранения даты рождения пользователя
    """
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Возвращает строковое представление пользователя
        """
        return self.username
