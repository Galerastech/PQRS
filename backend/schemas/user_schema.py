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
    tenant_id: int
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    tenant_id: Optional[int]
    name: str
    email: EmailStr
    phone: Optional[str]
    apartment: int
    is_superadmin: bool

    class Config:
        from_attributes = True
        orm_mode = True

class AdminSchemaRequest(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True
