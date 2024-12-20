from layouts import AuthLayout, MainLayout
from services.auth_service import UserRole
from views import LoginView, SuperAdminView

def get_routes(page):
    return {
        "/login": {
            "view": lambda: LoginView(page),
            "layout": AuthLayout,
            "public": True,
        },
        "/super-admin": {
            "view": lambda: SuperAdminView(page),
            "layout": MainLayout,
            "public": False,
            "role": UserRole.SUPER_ADMIN,
        },
    }