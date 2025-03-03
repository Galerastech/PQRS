from multiprocessing import AuthenticationError
from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.params import Depends
from backend.database import get_db
from backend.models import User
from backend.schemas import UserSchema, TokenSchema
from backend.security.security import create_access_token, authenticate_user, get_current_active_user

router = APIRouter(prefix="/auth", )


@router.post("/token", response_model=TokenSchema)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db),
):
    user = authenticate_user(db, email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.email,
              'tenant_id': user.tenant_id,
              'role': user.role,
              'email': user.email,
              }
    )
    return TokenSchema.model_validate(access_token)


@router.get("/users/me", response_model=UserSchema)
def read_users_me(current_user: User = Depends(get_current_active_user)) -> UserSchema:
    return current_user
