"""
Модуль для управления аутетификацией пользователя и предоставления доступа к страницам выбора и чтения книг
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import os


def register_user(request):
    """
    Функция для регистрации пользователя
    :return: Если регистрация прошла успешно, перенаправляет на страницу входа,
     если же нет, то обновляет страницу регистрации
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    """
    Функция для аутетификации пользователя
    :return: Если вход прошёл успешно, то перенаправляет на страницу выбора книги
    """
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password, username=username)
            if user is not None:
                login(request, user)
                return redirect('books')
            else:
                form.add_error(None, "Неправильный email или пароль.")
    return render(request, 'login.html', {'form': form})


BOOK_FILE1 = os.path.join('static', 'books', "L.Tolstoi_tom_1.txt")
BOOK_FILE2 = os.path.join('static', 'books', "igra-prestolov-248812.txt")


@login_required
def logout_user(request):
    """
    Функция для выхода пользователя из системы
    :return: Перенаправляет на страницу входа
    """
    logout(request)
    return redirect('login')


def book_lev_tolskoi():
    """
    Открывает файл с содержанием книги "Война и Мир" и считывает содержание построчно
    """
    with open(BOOK_FILE1, 'r') as file:
        return file.readlines()


def book_song_of_ice_and_fire():
    """
    Открывает файл с содержанием книги "Песнь льда и пламени" и считывает содержание построчно
    """
    with open(BOOK_FILE2, 'r') as file:
        return file.readlines()


@login_required
def reed_book1(request):
    """
    Обрабатывает запрос пользователя на чтение книги "Война и мир"

    Создаёт пагинацию книги и указываем параметры для пагинации
    Разбивает страницу по 30 строк
    """
    book_lines = book_lev_tolskoi()
    paginator = Paginator(book_lines, 30)
    page_number = request.GET.get('page')
    lines_to_display = paginator.get_page(page_number)

    return render(request, 'L.Tolstoi.html', {'context': lines_to_display, 'paginator': paginator})


@login_required
def reed_book2(request):
    """
    Обрабатывает запрос пользователя на чтение книги "Песнь льда и пламени"

    Создаёт пагинацию книги и указываем параметры для пагинации
    Разбивает страницу по 30 строк
    """
    book_lines = book_song_of_ice_and_fire()
    paginator = Paginator(book_lines, 30)
    page_number = request.GET.get('page', 1)
    lines_to_display = paginator.get_page(page_number)

    return render(request, 'game_of_the_thrones.html',
                  {'context': lines_to_display, 'paginator': paginator})


@login_required
def choosing_a_book(request):
    """
    Функция для вывода страницы выбора книги
    """
    return render(request, "books.html")
