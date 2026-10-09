from fastapi import FastAPI, Depends
from typing import Annotated
from database import engine, Base
from models import User, Contact
from database import get_db
from sqlalchemy.orm import Session
from schemas import CommonResponse, UserData
from helper_functions import validate_user

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"health": "FastAPI is running"}


@app.post("/submit", response_model=CommonResponse)
async def add_user(user: UserData, db: Annotated[Session, Depends(get_db)]):

    email, name, msg = await validate_user(user=user)

    return CommonResponse(message="form submitted successfully")
