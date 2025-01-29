from datetime import datetime, timedelta, UTC, timezone
from typing import Optional
import jwt
from sqlalchemy.orm import Session

from backend.models import User
from backend.schemas import UserSchema, TokenSchema
from config import settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

BOGOTA_TZ = timezone(timedelta(hours=-5))

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    now_utc =datetime.now(UTC)
    expire_utc = now_utc + (expires_delta or timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)))
    expire_utc = expire_utc.astimezone(BOGOTA_TZ)
    to_encode.update({"exp": expire_utc.timestamp()})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return TokenSchema(access_token=encoded_jwt, token_type="bearer", expires_in=expire_utc.strftime("%Y-%m-%d %H:%M:%S"))


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password(password: str) -> str:
    return pwd_context.hash(password)


def authenticate_user(db: Session, email: str, password: str) -> Optional[UserSchema]:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return UserSchema.model_validate(user)
