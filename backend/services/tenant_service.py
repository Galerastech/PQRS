from typing import List

from backend.models import Tenant
from backend.schemas import TenantLoginSchema


class TenantService:
    def get_tenants(self, db) -> List[TenantLoginSchema]:
        return db.query(Tenant).all()
