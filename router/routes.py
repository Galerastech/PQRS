from layouts import AuthLayout, SuperAdminLayout,AdminLayout, ResidentLayout
from pages import LoginPage, RegisterPage, SuperAdminDashboard, Dashboard, AdminDashboard


def get_routes(page):
    auth_layout = AuthLayout(page)
    super_admin_layout = SuperAdminLayout(page)
    admin_layout = AdminLayout(page)
    resident_layout = ResidentLayout(page)

    return {
        "/login": {"layout": auth_layout, "page": lambda: LoginPage(page).build()},
        "/register": {"layout": auth_layout, "page": lambda: RegisterPage(page).build()},
        "/superadmin-dashboard": {"layout": super_admin_layout, "page": lambda: SuperAdminDashboard(page).build()},
        "/administrator-dashboard": {"layout": admin_layout, "page": lambda: AdminDashboard(page).build()},
        "/dashboard": {"layout": resident_layout, "page": lambda: Dashboard(page).build()},
    }
def protected_routes():
    return {
        "/superadmin-dashboard": "superadministrator",
        "/administrator-dashboard": "administrador",
        "/dashboard": "residente",
    }