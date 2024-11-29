from datetime import timedelta

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.params import Depends
from backend.database import get_db
from backend.schemas import UserSchema, UserLoginSchema, TokenSchema
from backend.services import AuthService
from config import settings

router = APIRouter(prefix="/auth")

auth_service = AuthService()


@router.post("/signup", response_model=UserSchema)
async def signup(data: UserSchema, db: Session = Depends(get_db)):
    try:
        existing_user = auth_service.check_user_existence(db, data)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuario ya se encuentra en la base de datos")
        new_user = auth_service.create_user(db=db, user=data)
        return new_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/signin", response_model=UserLoginSchema)
async def login(data: UserLoginSchema, db: Session = Depends(get_db)):
    try:
        user = auth_service.authenticate_user(
            db, data.email,
            data.password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"}
            )
        access_token = auth_service.create_access_token(
            data={"sub": user.id},
            expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return TokenSchema(access_token=access_token, token_type="bearer", user=user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
