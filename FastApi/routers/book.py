from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi_pagination import Page
router = APIRouter()

templates = Jinja2Templates(directory="FastApi/templates")
BOOK_FILE1 = "L.Tolstoi_tom_1.txt"
BOOK_FILE2 = "igra-prestolov-248812.txt"


def book_lev_tolskoi():
    with open(BOOK_FILE1, 'r') as file:
        return file.readlines()


def book_song_of_ice_and_fire():
    with open(BOOK_FILE2, 'r') as file:
        return file.readlines()


@router.post("/war_and_peace")
def reed_book1(request: Request, page: int = 1):
    book_lines = book_lev_tolskoi()
    total_lines = len(book_lines)
    per_page = 38
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Page(page=page, total=total_lines, per_page=per_page)

    return templates.TemplateResponse("L.Tolstoi.html",
                                      {"request": request, "lines": lines_to_display, "pagination": pagination,
                                       "current_page": page})


@router.post('/game_of_the_thrones')
def reed_book2(request: Request, page: int = 1):
    book_lines = book_lev_tolskoi()
    total_lines = len(book_lines)
    per_page = 30
    start = (page - 1) * per_page
    end = start + per_page

    lines_to_display = book_lines[start:end]

    pagination = Pagination(page=page, total=total_lines, per_page=per_page)

    return templates.TemplateResponse("game_of_the_thrones.html",
                                      {"request": request, "lines": lines_to_display, "pagination": pagination,
                                       "current_page": page})


@router.post('/books')
async def choosing_a_book(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("books.html", {"request": request})
