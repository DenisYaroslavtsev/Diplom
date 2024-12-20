from fastapi import FastAPI
from FastApi.routers import auth

app = FastAPI()

app.include_router(auth.router)
