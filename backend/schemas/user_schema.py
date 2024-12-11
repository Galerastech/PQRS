from typing import Optional

from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    apartment: int

class UserRegister(UserBase):
    tenant_id: int
    password:str = constr(min_length=8)

class UserLoginSchema(BaseModel):
    id: Optional[int] = None
    tenant_id: int
    email: EmailStr
    password: Optional[str] = None


class UserSchema(UserBase):
    id: Optional[int]
    tenant_id: Optional[int]
    name: str
    email: EmailStr
    apartment: int
    role: str

    class Config:
        from_attributes = True

class AdminSchema(BaseModel):
    email: EmailStr
    password: Optional[str] = None

    class Config:
        from_attributes = True
