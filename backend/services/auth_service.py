from datetime import timedelta, datetime
from typing import Optional
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from backend.models import User
from pydantic import EmailStr
from backend.schemas import UserSchema
import jwt

from backend.schemas.user_schema import UserRegister
from config import settings


class AuthService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def check_user_existence(self, db: Session, user: User):
        return (
            db.query(User)
            .filter(
                User.tenant_id == user.tenant_id,
                User.email == user.email,
            )
            .first()
        )

    def get_password(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_user(self, db: Session, user: UserRegister) -> UserSchema:
        hashed_pwd = self.get_password(user.password)
        new_user = User(
            name=user.name,
            email=user.email,
            password=hashed_pwd,
            apartment=user.apartment,
            phone=user.phone,
            tenant_id=user.tenant_id,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserSchema.model_validate(new_user)

    def authenticate_user(
        self, db: Session, email: EmailStr, password: str
    ) -> Optional[UserSchema]:
        user = db.query(User).filter(User.email == email).first()
        if user and self.verify_password(password, user.password):
            return user
        return None

    def create_access_token(
        self, data: dict, expires_delta: Optional[timedelta] = None
    ) -> dict:
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire_minutes = int(settings.ACCESS_TOKEN_EXPIRE_MINUTES or 60)
            expire = datetime.now() + timedelta(minutes=expire_minutes)

        to_encode = data.copy()
        to_encode.update({"exp": int(expire.timestamp())})
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
        )
        return {
            "access_token": encoded_jwt,
            "token_type": "bearer",
            "expires_in": expire_minutes,
        }
