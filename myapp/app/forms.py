from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from datetime import date


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Введите ваш логин')
    email = forms.EmailField(label='Введите email', widget=forms.EmailInput)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(date.today().year - 70, date.today().year)))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'birth_date')


class LoginForm(AuthenticationForm):
    email = forms.CharField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
