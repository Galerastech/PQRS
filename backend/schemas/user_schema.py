from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class UserRegister(BaseModel):
    tenant_id: int
    name: str
    email: EmailStr
    password: constr(min_length=8)
    phone: str
    apartment: int


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    id : int
    tenant_id: Optional[int]
    name: str
    email: EmailStr
    phone: Optional[str]
    status: str
    apartment: int
    role: str

    class Config:
        from_attributes = True
        orm_mode = True

class AdminSchemaRequest(BaseModel):
    email: EmailStr
    password: str
    tenant_id: Optional[int] = None

    class Config:
        from_attributes = True
