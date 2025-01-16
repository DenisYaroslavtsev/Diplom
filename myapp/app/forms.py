"""
Модуль для создания формы регистрации и аутетификации пользователя
"""

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from datetime import date


class SignUpForm(UserCreationForm):
    """
    Форма регистрации нового пользователя

    Атрибуты:
        username(str): Логин пользователя
        email(Emailstr): Email пользователя
        birth_date(date): Дата рождения пользователя с диапозоном в 70 лет от текущей даты
        password2(str): Повтор пароля
    """
    username = forms.CharField(label='Введите ваш логин')
    email = forms.EmailField(label='Введите email', widget=forms.EmailInput)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year - 70, date.today().year)))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        """
        Данная функция нужна для изменения стандартного текста подсказок
        """
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''

    class Meta:
        """
        Настраивает поля формы
        """
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'birth_date')


class LoginForm(AuthenticationForm):
    """
    Форма аутетификации пользователя
    """
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
