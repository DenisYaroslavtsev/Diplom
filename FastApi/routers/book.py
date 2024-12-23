from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi_pagination import add_pagination, Page
import os

router = APIRouter(prefix='/books', tags=['books'])
templates = Jinja2Templates(directory="FastApi/templates")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_DIR = os.path.join(BASE_DIR, '../books')
BOOK_FILE1 = os.path.join(BOOK_DIR, "L.Tolstoi_tom_1.txt")
BOOK_FILE2 = os.path.join(BOOK_DIR, "igra-prestolov-248812.txt")


def book_lev_tolskoi():
    with open(BOOK_FILE1, 'r') as file:
        return file.readlines()


def book_song_of_ice_and_fire():
    with open(BOOK_FILE2, 'r') as file:
        return file.readlines()


@router.get("/war_and_peace")
def reed_book1(request: Request, page: int = 1):
    book_lines = book_lev_tolskoi()
    total_lines = len(book_lines)
    per_page = 38
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Page(page=page, total=total_lines, size=per_page, items=lines_to_display)

    return templates.TemplateResponse("L.Tolstoi.html",
                                      {"request": request, "lines": lines_to_display, "pagination": pagination,
                                       "current_page": page})


@router.get('/game_of_the_thrones')
def reed_book2(request: Request, page: int = 1):
    book_lines = book_song_of_ice_and_fire()
    total_lines = len(book_lines)
    per_page = 30
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Page(page=page, total=total_lines, size=per_page, items=lines_to_display)

    return templates.TemplateResponse("game_of_the_thrones.html",
                                      {"request": request, "lines": lines_to_display, "pagination": pagination,
                                       "current_page": page})


@router.get('/select_book')
async def choosing_a_book(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("books.html", {"request": request})
