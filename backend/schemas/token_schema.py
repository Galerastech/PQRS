from pydantic import BaseModel



class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    expires_in: int

    class Config:
        from_attributes = True
