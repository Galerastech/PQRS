from ast import In
from datetime import timedelta
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse, RedirectResponse
import jwt
from sqlalchemy.orm import Session
from fastapi.params import Depends
from backend.database import get_db
from backend.models import Tenant
from backend.schemas import UserSchema, UserLoginSchema, TokenSchema
from backend.schemas import user_schema
from backend.schemas.user_schema import UserRegister, AdminSchema
from backend.services import AuthService
from config import settings
from backend.security.security import create_access_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/superuser")
oauth2_scheme_user = OAuth2PasswordBearer(tokenUrl="auth/signin")

auth_service = AuthService()
@router.post("/signup", response_model=UserSchema)
async def signup(data: UserRegister, db: Session = Depends(get_db)):
    try:
        existing_user = auth_service.check_user_existence(db, data)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuario ya se encuentra en la base de datos")
        new_user = auth_service.create_user(db=db, user=data)
        return UserSchema.model_validate(new_user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/signin", response_model=TokenSchema)
async def login(data: UserLoginSchema, db: Session = Depends(get_db)):
    try:
        user = auth_service.authenticate_user(
            db, data.email,
            data.password)
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado",
                headers={"WWW-Authenticate": "Bearer"}
            )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales invalidas",
                headers={"WWW-Authenticate": "Bearer"}
            )

        access_token = create_access_token(
            data={"sub": user.id, 'email': user.email, 'role': user.role},
            expires_delta=timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        )
        return TokenSchema(access_token=access_token, token_type="bearer",
                           expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/superuser", response_model=TokenSchema)
def superuser(data: AdminSchema, db: Session = Depends(get_db)):
    try:
        user = auth_service.authenticate_user(
            db, data.email,
            data.password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Credenciales invalidas",
                headers={"WWW-Authenticate": "Bearer"}
            )
            
        access_token = create_access_token(
            data={"sub": user.id, 'email': user.email, 'role': user.role}
        )
        response = JSONResponse(content={"access_token": access_token, "token_type": "bearer"})
        response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="lax", secure=True)
        return response

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
