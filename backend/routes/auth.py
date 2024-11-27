from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm

from backend.database import get_db
from backend.schemas import RegisterSchema
from backend.services import AuthService

router = APIRouter(prefix="/auth")

auth_service = AuthService()


@router.post("/signup", response_model=RegisterSchema)
async def signup(data:RegisterSchema , db: Session = Depends(get_db)):
    existing_user = auth_service.check_user_existence(db, data)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya se encuentra en la base de datos")
    new_user = auth_service.create_user(db=db, user=data)
    return new_user

# @router.post("/login", response_model=schemas.UserSchema)
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = auth_service.authenticate_user(db, form_data.username, form_data.password)
