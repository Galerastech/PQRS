from functools import wraps
from typing import Callable, Optional

from services.auth_service import UserRole


def require_auth(view_func: Optional[Callable] = None, role: Optional[UserRole] = None):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            auth_service = self.page.auth_service
            
            if not auth_service.is_authenticated():
                self.page.go("/login")
                return None
                
            if role and not auth_service.has_role(role):
                # Redirigir según el rol actual
                current_role = auth_service.get_user_role()
                default_routes = {
                    UserRole.SUPER_ADMIN: "/superadmin-dashboard",
                    UserRole.ADMIN: "/admin-dashboard",
                    UserRole.RESIDENT: "/dashboard"
                }
                self.page.go(default_routes.get(current_role, "/login"))
                return None
                
            return await func(self, *args, **kwargs)
        return wrapper
    
    if view_func is None:
        return decorator
    return decorator(view_func)