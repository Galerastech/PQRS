from typing import List

from fastapi import APIRouter
from backend.database import get_db
from fastapi.params import Depends
from sqlalchemy.orm import Session
from backend.models import Tenant
from backend.schemas import TenantLoginSchema

router = APIRouter()




@router.get('/tenants', response_model=List[TenantLoginSchema])
async def list_tenants(db: Session = Depends(get_db)):
    tenants = db.query(Tenant).all()
    return tenants