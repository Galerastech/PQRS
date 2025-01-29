from datetime import datetime, timedelta
from multiprocessing import AuthenticationError
from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from fastapi.security import  OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.params import Depends
from backend.database import get_db
from backend.schemas import UserSchema, TokenSchema
from backend.schemas.user_schema import UserRegister
from backend.security.security import create_access_token, authenticate_user

from config import settings

router = APIRouter(prefix="/auth")


@router.post("/token")
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    try:
        user = authenticate_user(
            db, email=form_data.username, password=form_data.password
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas Verifique nuevamente",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(
            data={"sub": str(user.id), "tenant_id": user.tenant_id, "role": user.role}
        )
        return access_token
    except AuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    @router.get("/users/me")
    def read_users_me(current_user: UserSchema = Depends(auth_service.get_current_active_user)):
        return current_user