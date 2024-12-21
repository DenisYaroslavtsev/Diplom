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


@router.post('/register')
async def register_user(db: Annotated[Session, Depends(get_db)], user: UserResponse):
    if user.username == user.password:
        # raise HTTPException(status_code=400, detail="Пароль не должен совпадать с логином!")
        return JSONResponse(status_code=400, content={"error": "Пароль не должен совпадать с логином"})

    if user.password != user.repeat_password:
        # raise HTTPException(status_code=400, detail="Пароли не совпадают!")
        return JSONResponse(status_code=400, content={"error": "Пароли не совпадают"})

    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user == user.username:
        # raise HTTPException(status_code=400, detail="Данный логин уже занят!")
        return JSONResponse(status_code=400, content={"error": "Данный логин уже занят"})
    is_existence_user = db.query(User).filter(User.email == user.email).first()
    if in_existence_user == user.email:
        # raise HTTPException(status_code=400, detail="Данный email уже занят!")
        return JSONResponse(status_code=400, content={"error": "Данный email уже занят"})

    hashed_password = pass_context.hash(user.password)
    db_user = User(username=user.username, password=hashed_password, birth_day=user.birth_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # contex = {'username': user.username,
    #           'password': hashed_password,
    #           'email': user.email,
    #           'birth_date': user.birth_date}
    # print(contex)

    return RedirectResponse(url="/auth/login")


@router.post('/login')
async def login_user(db: Annotated[Session, Depends(get_db)], user: CreateUser):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pass_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Неправильно введён email или пароль")

    return RedirectResponse(url='/upload', status_code=303)


@router.get('/register')
async def get_register_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("register.html", {"request": request})


@router.get('/login')
async def get_login_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("login.html", {"request": request})


