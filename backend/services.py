from typing import Type

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from backend.models import User
from backend.schemas import UserSchema


class UserService:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, password: str) -> bool:
        return self.pwd_context.verify(password, self.pwd_context.hash(password))

    def create_user(self, db: Session, user: UserSchema) -> User:
        hashed_pwd = self.get_password(user.password)
        new_user = User(
            username=user.username,
            email=user.email,
            password=hashed_pwd
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def authenticate_user(self, db: Session, email: str, password: str) -> Type[User] | None:
        user = db.query(User).filter(User.email == email).first()
        if not user or not self.verify_password(password, user.password):
            return None
        return user
