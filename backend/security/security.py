from datetime import datetime, timedelta
from typing import Optional
import jwt
from config import settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None)->str:
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire_minutes = int(settings.ACCESS_TOKEN_EXPIRE_MINUTES or 60)
        expire = datetime.now() + timedelta(minutes=expire_minutes)

    to_encode = data.copy()
    to_encode.update({"exp": int(expire.timestamp())})
    if settings.SECRET_KEY is None:
        raise ValueError("SECRET_KEY must not be None")
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_password(plain_password:str, hashed_password:str)->bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password(password:str)->str:
    return pwd_context.hash(password)