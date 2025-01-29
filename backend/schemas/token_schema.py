from pydantic import BaseModel

from backend.schemas import UserSchema


class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    expires_in: str

    class Config:
        from_attributes = True
