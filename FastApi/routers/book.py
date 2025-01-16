"""
Модуль для чтения книг

Данный модуль представляет API для чтения книг Л. Толстого "Война и Мир" и Дж. Мартина "Песнь льда и пламени".
Книги разбиты на страницы (каждая из которых содержит по 30 строк), которые можно листать с помощью пагинации
Доступ к книгам есть только у авторизованных пользователей

Создаёт роутеры для страниц: "выбор книги", книги "Война и мир", книги "Песнь льда и пламени"
"""

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi_pagination import Page, add_pagination
import os

router = APIRouter(prefix='/books', tags=['books'])
templates = Jinja2Templates(directory="FastApi/templates")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_DIR = os.path.join(BASE_DIR, '../books')
BOOK_FILE1 = os.path.join(BOOK_DIR, "L.Tolstoi_tom_1.txt")
BOOK_FILE2 = os.path.join(BOOK_DIR, "igra-prestolov-248812.txt")


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


@router.get("/war_and_peace")
def reed_book1(request: Request, page: int = 1):
    """
    Обрабатывает запрос пользователя на чтение книги "Война и мир"

    :param request: Объект запроса, содержащий данные сессии
    :param page: Задаём параметр номера страницы по умолчанию 1
    :return: Ответ с отображением страницы с книгой или перенапралвнеие на страницу входа

    Создаёт пагинацию книги и указываем параметры для пагинации
    Разбивает страницу по 30 строк
    """
    user_id = request.session.get('user_id')
    if user_id is None:
        error_message = 'Вы должны быть авторизованы, чтобы получить доступ к этой странице.'
        return templates.TemplateResponse("login.html", {"request": request,
                                                         "error": error_message})
    book_lines = book_lev_tolskoi()
    total_lines = len(book_lines)
    per_page = 30
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Page(page=page, total=total_lines, size=per_page, items=lines_to_display)

    return templates.TemplateResponse("L.Tolstoi.html",
                                      {"request": request, "lines": lines_to_display, "pagination": pagination})


@router.get('/game_of_the_thrones')
def reed_book2(request: Request, page: int = 1):
    """
    Обрабатывает запрос пользователя на чтение книги "Песнь льда и пламени"

    :param request: Объект запроса, содержащий данные сессии
    :param page: Задаём параметр номера страницы по умолчанию 1
    :return: Ответ с отображением страницы с книгой или перенапралвнеие на страницу входа

    Создаёт пагинацию книги и указываем параметры для пагинации
    Разбивает страницу по 30 строк
    """
    user_id = request.session.get('user_id')
    if user_id is None:
        error_message = 'Вы должны быть авторизованы, чтобы получить доступ к этой странице.'
        return templates.TemplateResponse("login.html", {"request": request,
                                                         "error": error_message})
    book_lines = book_song_of_ice_and_fire()
    total_lines = len(book_lines)
    per_page = 30
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Page(page=page, total=total_lines, size=per_page, items=lines_to_display)

    return templates.TemplateResponse("game_of_the_thrones.html",
                                      {"request": request, "lines": lines_to_display, "pagination": pagination})


@router.get('/select_book')
async def choosing_a_book(request: Request):
    """
    Отображает страницу выбора книг, если пользователь не авторизован, то доступ будет закрыт
    """
    user_id = request.session.get('user_id')
    if user_id is None:
        error_message = 'Вы должны быть авторизованы, чтобы получить доступ к этой странице.'
        return templates.TemplateResponse("login.html", {"request": request,
                                                         "error": error_message})

    return templates.TemplateResponse("books.html", {"request": request})


add_pagination(router)
