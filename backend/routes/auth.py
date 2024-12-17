from datetime import timedelta
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/signup", response_model=UserSchema)
async def signup(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
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


#  TODO: Verificar que lo que realmente necesito se muestre en el dahsboard tanto del super admin comoo del admin
@router.post("/login", response_model=UserSchema)
async def login(data: UserLoginSchema, db: Session = Depends(get_db)):
    try:
        user = auth_service.authenticate_user(
            db, data.email,
            data.password)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas verifique nuevamente",
                headers={"WWW-Authenticate": "Bearer"}
            )

        
        return UserSchema.model_validate(user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )