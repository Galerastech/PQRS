from layouts import AuthLayout, MainLayout
from services.auth_service import UserRole
from views import LoginView


def get_routes(page):
    return {
        "/login": {
            "view": lambda: LoginView(page),
            "layout": AuthLayout,
            "public": True,
        },
        "/super-admin": {
            "view": lambda: SuperAdminDashboard(page),
            "layout": MainLayout,
            "protected": True,
            "role": [UserRole.ADMIN, UserRole.SUPER_ADMIN],
        },
    }
