from datetime import datetime, timedelta, UTC, timezone
from typing import Optional
import jwt
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import User
from backend.schemas import UserSchema, TokenSchema
from config import settings
from passlib.context import CryptContext
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

BOGOTA_TZ = timezone(timedelta(hours=-5))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password(password: str) -> str:
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str) -> Optional[UserSchema]:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return UserSchema.model_validate(user)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    now_utc = datetime.now(UTC)
    expire_utc = now_utc + (expires_delta or timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)))
    expire_utc = expire_utc.astimezone(BOGOTA_TZ)
    to_encode.update({"exp": expire_utc.timestamp()})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return TokenSchema(access_token=encoded_jwt, token_type="bearer",
                       expires_in=expire_utc.strftime("%Y-%m-%d %H:%M:%S"))


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return UserSchema.model_validate(user)


async def get_current_active_user(current_user: User = Depends(get_current_user)) -> Optional[UserSchema]:
    if current_user.role not in ['resident', 'administrator', 'superadmin']:
        raise HTTPException(status_code=400, detail="Rol de usuario no válido")

    if current_user.status == 'inactive':
        raise HTTPException(status_code=400, detail="Usuario inactivo")

    return current_user

