from layouts import AuthLayout
from pages import LoginPage, RegisterPage
from pages.super_admin_page import SuperAdminPage


def get_routes(page):
    auth_layout = AuthLayout(page)

    return {
        "/login": {"layout": auth_layout, "page": lambda: LoginPage(page).build()},
        "/register": {"layout": auth_layout, "page": lambda: RegisterPage(page).build()},
        "/super_admin": {"layout": auth_layout, "page": lambda: SuperAdminPage(page).build()},
    }
