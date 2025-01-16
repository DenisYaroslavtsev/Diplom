"""
Основной модуль для работы всего приложения
Модуль включает в себя управление аутетификацией, выбор и просмотр книг.Так же создаёт основные маршруты

Включает в себя функции регистрации, входа/выхода пользователя, авторизации, выбора книг, а так же чтение книги

Книги разбиты на страницы (каждая из которых содержит по 30 строк), которые можно листать с помощью пагинации
"""

from flask import Flask, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from Flask.backend.db import get_db
from Flask.models.models import User
from schemas import UserResponse, CreateUser
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination

app = Flask(__name__)

app.config['SECRET_KEY'] = 'very Very very Secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def login_auth(f):
    """
    Декоратор для защиты основных маршрутов, требующих аутетификацию пользователя

    :return: Сохраняет имя оригинальной функции
    """

    def wrap(*args, **kwargs):
        """
        Функция для проверки авторизации пользователя, принимает в себя произвольные аргументы

        :param args:
        :param kwargs:
        :return: Если пользователь авторизован, перенаправляет на страницу входа, если же нет - выводит ошибку
        """
        if 'user_id' not in session:
            flash("Вы должны войти в систему, чтобы получить доступ к этой странице.", "error")
            return redirect(url_for('login_user'))
        return f(*args, **kwargs)

    wrap.__name__ = f.__name__
    return wrap


@app.route('/', methods=['GET'])
def home():
    """
    Функция задаёт стартовую страницу регистрации по маршруту '/'
    """
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_user():
    """
    Функция для регистрации и проверки пользователя в БД
    Если данные будут введены не верно, будет выведена ошибка, если пользователя нет в БД, то он будет добавлен

    Если пользователь успешно прошёл регистрацию, перенаправляет на страницу входа, если нет, то перенаправляет
    на страницу регистрации заново
    """
    if request.method == 'POST':
        user = UserResponse(**request.form)

        if not user.email:
            flash("Email должен быть введён обязательно!", "error")
            return redirect(url_for('home'))

        if user.username == user.password:
            flash("Пароль не должен совпадать с логином!", "error")
            return redirect(url_for('home'))

        if user.password != user.repeat_password:
            flash("Пароли не совпадают!", "error")
            return redirect(url_for('home'))

        db: Session = get_db()
        existing_user = db.query(User).filter_by(username=user.username).first()

        if existing_user:
            flash("Данный логин уже занят", "error")
            return redirect(url_for('home'))

        existing_email = db.query(User).filter_by(email=user.email).first()
        if existing_email:
            flash("Данный email уже занят", "error")
            return redirect(url_for('home'))

        hashed_password = generate_password_hash(user.password)
        db_user = User(username=user.username, password=hashed_password, email=user.email, birth_day=user.birth_date)
        db.add(db_user)
        db.commit()

        return redirect(url_for('login_user'))

    return render_template('register.html')


@app.route('/login', methods=['POST', 'GET'])
def login_user():
    """
    Функция для входа пользователя. Производит проверку пользователя из БД
    Если введённые данные введены неправильно, то выводит ошибку, если всё верно, то перенаправляет на страницу выбора
    книги
    """
    if request.method == 'POST':
        user_data = CreateUser(**request.form)
        db_session: Session = get_db()
        db_user = db_session.query(User).filter_by(email=user_data.email).first()

        if db_user and check_password_hash(db_user.password, user_data.password):
            session['user_id'] = db_user.id
            return redirect(url_for('choosing_a_book'))

        flash("Неправильно введён email или пароль", "error")
        return redirect(url_for('login_user'))

    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout_user():
    """
    Функция для удаления пользователя из сессии(выход)

    :return: Перенаправляет после выхода на страницу входа
    """
    session.pop('user_id', None)
    flash("Вы успешно вышли из системы", "success")
    return redirect(url_for('login_user'))


BOOK_FILE1 = "L.Tolstoi_tom_1.txt"
BOOK_FILE2 = "igra-prestolov-248812.txt"


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


@app.route("/war_and_peace", methods=["GET", "POST"])
@login_auth
def reed_book1():
    """
    Обрабатывает запрос пользователя на чтение книги "Война и мир"

    Создаёт пагинацию книги и указываем параметры для пагинации
    Разбивает страницу по 38 строк
    """
    book_lines = book_lev_tolskoi()
    total_lines = len(book_lines)
    page = request.args.get('page', type=int, default=1)
    per_page = 38
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Pagination(page=page, total=total_lines, per_page=per_page)

    return render_template('L.Tolstoi.html', lines=lines_to_display,
                           pagination=pagination, current_page=page)


@app.route('/game_of_the_thrones', methods=["GET", "POST"])
@login_auth
def reed_book2():
    """
    Обрабатывает запрос пользователя на чтение книги "Песнь льда и пламени"

    Создаёт пагинацию книги и указываем параметры для пагинации
    Разбивает страницу по 38 строк
    """
    book_lines = book_song_of_ice_and_fire()
    total_lines = len(book_lines)
    page = request.args.get('page', type=int, default=1)
    per_page = 38
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Pagination(page=page, total=total_lines, per_page=per_page)

    return render_template('game_of_the_thrones.html', lines=lines_to_display,
                           pagination=pagination, current_page=page)


@app.route('/books', methods=['GET', 'POST'])
@login_auth
def choosing_a_book():
    """
    Функция для отображения страницы выбора книги
    """
    return render_template('books.html')


if __name__ == '__main__':
    app.run()
