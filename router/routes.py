from ast import Not
from httpx import Auth
from layouts import AuthLayout, MainLayout
from pages import LoginPage, RegisterPage, NotFoundPage
from pages.super_admin_dashboard import SuperAdminDashboard


def get_routes(page):

    return {
        "/": {"layout": AuthLayout(page), "page": lambda: LoginPage(page).build()},
        "/register": {"layout": AuthLayout(page), "page": lambda: RegisterPage(page).build()},
        "/404": {"layout": MainLayout(page), "page": lambda: NotFoundPage(page).build()},
        "/super-admin-dashboard": {"layout": MainLayout(page), "page": lambda: SuperAdminDashboard(page).build()},
        "/admin-dashboard": {"layout": MainLayout(page), "page": lambda: AdminDashboard(page).build(),"protected": True, "role": "administrador"},
        "/dashboard": {"layout": MainLayout(page), "page": lambda: Dashboard(page).build(),"protected": True, "role": "residente"},
        "/unauthorized": {"layout": MainLayout(page), "page": lambda: Unauthorized(page).build(),"protected": True, "role": ["residente", "administrador, superadmin"]},
    }
