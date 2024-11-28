from pydantic import BaseModel


class UserSchema(BaseModel):
    tenant_id: int
    name: str
    email: str
    password: str
    phone: str
    apartment: int

    class Config:
        from_attributes = True
