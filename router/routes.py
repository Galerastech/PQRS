from layouts import AuthLayout
from layouts import SuperAdminLayout
from pages import LoginPage, RegisterPage
from pages.super_admin_page import SuperAdminPage


def get_routes(page):
    auth_layout = AuthLayout(page)

    # TODO: implementar layouts y page
    super_admin_layout = SuperAdminLayout(page)
    return {
        "/login": {"layout": auth_layout, "page": lambda: LoginPage(page).build()},
        "/register": {"layout": auth_layout, "page": lambda: RegisterPage(page).build()},
        "/super_admin": {"layout": super_admin_layout, "page": lambda: SuperAdminPage(page).build()},
    }
