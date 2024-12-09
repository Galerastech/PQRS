from typing import List

from backend.models import Tenant
from backend.schemas import TenantLoginSchema
from sqlalchemy.orm import Session


class TenantService:
    def get_tenants(self, db: Session) -> List[TenantLoginSchema]:
        return [TenantLoginSchema.model_validate(tenant) for tenant in db.query(Tenant).all()]
