from pydantic import BaseModel


class TenantLoginSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
