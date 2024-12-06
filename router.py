import flet as ft

from layouts.auth_layout import AuthLayout
from layouts.navbar_layout import Navbar_layout
from pages import LoginPage
from pages.register_page import RegisterPage
from pages.SuperAdministrador.menu import MenuPage
from services import AuthService

ROUTES = {
    "/login": lambda page: AuthLayout(LoginPage(page)),
    "/register": lambda page: AuthLayout(RegisterPage(page)),
    #add route superadministrador
    #todo: check navbar and Menu
    "/superadministrador/menu": lambda page: Navbar_layout(MenuPage)
}


class Router:
    def __init__(self, page: ft.Page):
        self.page = page

    def navigate(self, route: str):
       self.page.controls.clear()
       view = ROUTES.get(route, lambda page: ft.Text("404 Not Found"))
       self.page.add(view(self.page))
       self.page.update()
