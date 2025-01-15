from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from FastApi.routers import auth, book
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="FastApi/static"), name="static")
app.mount("/static", StaticFiles(directory="FastApi/static/images"), name="images")


@app.get('/')
async def home_page():
    return RedirectResponse(url='/auth/register')


app.add_middleware(SessionMiddleware, secret_key="veryVerysecretKey")
app.include_router(auth.router)
app.include_router(book.router)
