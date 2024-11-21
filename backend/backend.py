from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import crud

from backend import schemas
from backend.database import get_db
from backend.models import User
from backend.schemas import UserSchema
from backend.services import UserService

app = FastAPI(
    title="PQRS",
    docs_url="/app/docs",

)

user_service = UserService()


@app.post("/auth/signup",tags=["Auth"])
async def sign_up(user: UserSchema, db: Session = Depends(get_db)):
    exist_user = db.query(User).filter(
        (User.email == user.email) |
        (User.username == user.username)
    ).first()

    if exist_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe en la base de datos")
    new_user = user_service.create_user(db=db, user=user)
    return new_user
