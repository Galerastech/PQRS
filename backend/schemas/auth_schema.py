from pydantic import BaseModel,EmailStr


class RegisterSchema(BaseModel):
    tenant: int
    username: str
    email: EmailStr
    password: str

    class Config:
        from_atributes = True