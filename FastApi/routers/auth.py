from fastapi import APIRouter, Depends, status, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from FastApi.backend.db_depends import get_db
from FastApi.shemas import UserResponse, CreateUser
from typing import Annotated
from passlib.context import CryptContext
from FastApi.models.user import User
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

templates = Jinja2Templates(directory="FastApi/templates")
router = APIRouter(prefix='/auth', tags=['Auth'])

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# @router.post('/register')
# async def register_user(request: Request, db: Annotated[Session, Depends(get_db)], user: UserResponse):
#     form_data = await request.form()
#     username = form_data.get('username')
#     password = form_data.get('password')
#     repeat_password = form_data.get('repeat_password')
#     email = form_data.get('email')
#     birth_date = form_data.get('birth_date')
#     if username == password:
#         # raise HTTPException(status_code=400, detail="Пароль не должен совпадать с логином!")
#         return JSONResponse(status_code=400,
#                             content={"request": request, "error": "Пароль не должен совпадать с логином"})
#
#     if password != repeat_password:
#         # raise HTTPException(status_code=400, detail="Пароли не совпадают!")
#         return JSONResponse(status_code=400, content={"request": request, "error": "Пароли не совпадают"})
#
#     existing_user = db.query(User).filter(User.username == username).first()
#     if existing_user == user.username:
#         # raise HTTPException(status_code=400, detail="Данный логин уже занят!")
#         return JSONResponse(status_code=400, content={"request": request, "error": "Данный логин уже занят"})
#     is_existence_user = db.query(User).filter(User.email == email).first()
#     if is_existence_user == user.email:
#         # raise HTTPException(status_code=400, detail="Данный email уже занят!")
#         return JSONResponse(status_code=400, content={"request": request, "error": "Данный email уже занят"})
#
#     hashed_password = pass_context.hash(password)
#     db_user = User(username=username, password=hashed_password, email=email, birth_day=birth_date)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#
#     return RedirectResponse(url="/auth/login", status_code=303)

@router.post('/register')
async def register_user(request: Request, db: Annotated[Session, Depends(get_db)]):
    form_data = await request.form()
    username = form_data.get('username')
    password = form_data.get('password')
    repeat_password = form_data.get('repeat_password')
    email = form_data.get('email')
    birth_date = form_data.get('birth_date')

    # Проверки
    if password == username:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пароль не должен совпадать с логином!"})

    if password != repeat_password:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пароли не совпадают!"})

    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Данный логин уже занят!"})

    is_existence_user = db.query(User).filter(User.email == email).first()
    if is_existence_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Данный email уже занят!"})

    # Хеширование пароля и создание пользователя
    hashed_password = pass_context.hash(password)
    db_user = User(username=username, password=hashed_password, email=email, birth_day=birth_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Перенаправление на страницу логина
    return RedirectResponse(url="/auth/login", status_code=303)


@router.post('/login')
async def login_user(request: Request, db: Annotated[Session, Depends(get_db)], user: CreateUser):
    form_data = await request.form()
    email = form_data.get('email')
    password = form_data.get('password')
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user or not pass_context.verify(password, db_user.password):
        return templates.TemplateResponse("login.html", {"request": request, "error": "Неправильно введён email или пароль!"})

    return RedirectResponse(url='/upload', status_code=303)


@router.get('/register')
async def get_register_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("register.html", {"request": request})


@router.get('/login')
async def get_login_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("login.html", {"request": request})
