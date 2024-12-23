from pydantic import BaseModel
from datetime import date

class CreateUser(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    username: str
    email: str
    password: str
    repeat_password: str
    birth_date: date
