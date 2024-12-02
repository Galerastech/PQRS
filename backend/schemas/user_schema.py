from pydantic import BaseModel


# TODO: cambiar los schemas segun las peticiones y lo que realmente se necesita manteniedo la seguridad de los datos
class UserSchema(BaseModel):
    tenant_id: int
    name: str
    email: str
    password: str
    phone: str
    apartment: int

    class Config:
        from_attributes = True


class UserLoginSchema(BaseModel):
    tenant_id: int
    email: str
    password: str

    class Config:
        from_attributes = True

        # from pydantic import BaseModel, EmailStr, constr
        #
        # class UserRegisterSchema(BaseModel):
        #     name: str
        #     email: EmailStr
        #     password: constr(min_length=8)
        #     phone: str
        #     apartment: int
        #
        # class UserLoginSchema(BaseModel):
        #     email: EmailStr
        #     password: str
        #
        # class UserSchema(BaseModel):
        #     tenant_id: int
        #     name: str
        #     email: EmailStr
        #     phone: str
        #     apartment: int
        #     is_admin: bool
        #
        #     class Config:
        #         orm_mode = True  # Necesario para convertir desde el modelo ORM
        #
        # class TokenSchema(BaseModel):
        #     access_token: str
        #     token_type: str = "bearer"
        #     user: UserSchema  # Aquí también se necesita orm_mode si se devuelve un objeto ORM
        #
        # # Esquema para la respuesta del registro (opcional)
        # class UserResponseSchema(UserSchema):
        #     pass  # Puedes extender o modificar según sea necesario

# https://www.perplexity.ai/search/como-hacer-downgrade-en-alembi-cL1z4WRJSRGyeqomz1PFxQ
