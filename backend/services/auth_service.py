from datetime import timedelta, datetime
from re import U
from typing import Optional
from sqlalchemy.orm import Session
from backend.models import User
from pydantic import EmailStr
from backend.schemas import UserSchema
from backend.security.security import verify_password, get_password
from backend.schemas.user_schema import UserRegister
from config import settings


class AuthService:
    # check user
    def check_user_existence(self, db: Session, user: User):
        return db.query(User).filter(
            User.email == user.email
        ).first()

    # create user
    def create_user(self, db: Session, user: UserRegister) -> UserSchema:
        hashed_pwd = get_password(user.password)
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
    
    # authenticate user
    def authenticate_user(self, db: Session, email: EmailStr, password: str) -> Optional[UserSchema]:
        user = db.query(User).filter(User.email == email).first()
        if user and verify_password(password, user.password):
            return user
        return None