from pydantic import BaseModel

from backend.schemas import UserSchema


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    user: UserSchema

    class Config:
        from_attributes = True
