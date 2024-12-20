from pydantic import EmailStr, BaseModel
from datetime import date


class UserResponse(BaseModel):
    username: str
    password: str
    repeat_password: str
    email: EmailStr
    birth_date: date


class CreateUser(BaseModel):
    email: EmailStr
    password: str
