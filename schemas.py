from pydantic import BaseModel, EmailStr
from http import HTTPStatus


class CommonResponse(BaseModel):
    message: str
    status: int = HTTPStatus.OK


class UserData(BaseModel):
    name: str
    email: EmailStr
    message: str | None = None
