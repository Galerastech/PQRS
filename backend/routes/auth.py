from datetime import datetime, timedelta
from multiprocessing import AuthenticationError
from typing import Annotated
from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.params import Depends
from backend.database import get_db
from backend.schemas import UserSchema, UserLoginSchema, TokenSchema
from backend.schemas.user_schema import UserRegister
from backend.services import AuthService
from config import settings

router = APIRouter(prefix="/auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

auth_service = AuthService()


@router.post("/token", response_model=TokenSchema)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    try:
        user = auth_service.authenticate_user(
            db, email=form_data.username, password=form_data.password
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas Verifique nuevamente",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = auth_service.create_access_token(
            data={"sub": str(user.id), "tenant_id": user.tenant_id, "role": user.role}
        )
        return TokenSchema.model_validate(access_token)
    except AuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
