from ast import Not
from httpx import Auth
from layouts import AuthLayout, MainLayout
from views import LoginView


def get_routes(page):
    return {
        "/login": {
            "view": lambda: LoginView(page),
            "layout": AuthLayout,
            "public": True,
        },
        "/superadmin-dashboard": {
            "view": lambda: SuperAdminDashboard(page),
            "layout": MainLayout,
            "protected": True,
            "role": "superadmin",
        },
    }
