import flet as ft

from layouts import AuthLayout, MainLayout
from pages import LoginPage
from pages import RegisterPage
from pages.principal import MainPage
from services import AuthService

ROUTES = {
    "/login": lambda page: AuthLayout(LoginPage(page)),
    "/register": lambda page: AuthLayout(RegisterPage(page)),
    "/mainpage": lambda page: MainLayout(MainPage(page))
}


class Router:
    def __init__(self, page: ft.Page):
        self.page = page

    def navigate(self, route: str):
        self.page.controls.clear()
        view = ROUTES.get(route, lambda page: ft.Text("404 Not Found"))
        self.page.add(view(self.page))
        self.page.update()
