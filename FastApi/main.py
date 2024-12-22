from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from FastApi.routers import auth
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="FastApi/static"), name="static")

@app.get('/')
async def home_page():
    return RedirectResponse(url='/auth/register')

app.include_router(auth.router)
