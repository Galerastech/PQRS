from typing import List

from fastapi import APIRouter
from backend.database import get_db
from fastapi.params import Depends
from sqlalchemy.orm import Session
from backend.models import Tenant
from backend.schemas import TenantLoginSchema
from backend.services import TenantService

router = APIRouter()

tenant_service = TenantService()

@router.get('/tenants', response_model=List[TenantLoginSchema])
async def list_tenants(db: Session = Depends(get_db)):
    return tenant_service.get_tenants(db)