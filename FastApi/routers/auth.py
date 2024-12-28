from fastapi import APIRouter, Cookie, Depends, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import date
from typing import Annotated
from FastApi.backend.db_depends import get_db
from FastApi.models.user import User

templates = Jinja2Templates(directory="FastApi/templates")
router = APIRouter(prefix='/auth', tags=['Auth'])

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBasic()


def verify_user(credentials: HTTPBasicCredentials, db: Session):
    user = db.query(User).filter(User.email == credentials.username).first()
    if user and pass_context.verify(credentials.password, user.password):
        return user
    return None


@router.post('/register')
async def register_user(request: Request, db: Annotated[Session, Depends(get_db)]):
    form_data = await request.form()
    username = form_data.get('username')
    password = form_data.get('password')
    repeat_password = form_data.get('repeat_password')
    email = form_data.get('email')
    birth_date = form_data.get('birth_date')
    birth_date = date.fromisoformat(birth_date)

    if password == username:
        return templates.TemplateResponse("register.html",
                                          {"request": request, "error": "Пароль не должен совпадать с логином!"})

    if password != repeat_password:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Пароли не совпадают!"})

    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Данный логин уже занят!"})

    is_existence_user = db.query(User).filter(User.email == email).first()
    if is_existence_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Данный email уже занят!"})

    hashed_password = pass_context.hash(password)
    db_user = User(username=username, password=hashed_password, email=email, birth_day=birth_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return RedirectResponse(url="/auth/login", status_code=303)


@router.post('/login')
async def login_user(request: Request, db: Annotated[Session, Depends(get_db)]):
    form_data = await request.form()
    email = form_data.get('email')
    password = form_data.get('password')
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user or not pass_context.verify(password, db_user.password):
        return templates.TemplateResponse("login.html",
                                          {"request": request, "error": "Неправильно введён email или пароль!"})
    request.session['user_id'] = db_user.id

    return RedirectResponse(url='/books/select_book', status_code=303)


@router.post('/logout')
async def logout_user(request: Request):
    request.session.pop('user_id', None)
    return RedirectResponse(url='/auth/login', status_code=303)


@router.get('/register')
async def get_register_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("register.html", {"request": request})


@router.get('/login')
async def get_login_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("login.html", {"request": request})
