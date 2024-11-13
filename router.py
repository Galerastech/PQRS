import flet as ft

from layouts.auth_layout import AuthLayout
from pages import LoginPage

ROUTES = {
    "/login": lambda page: AuthLayout(LoginPage(page)),
}


class Router:
    def __init__(self, page: ft.Page):
        self.page = page

    def navigate(self, route: str):
       self.page.controls.clear()
       view = ROUTES.get(route, lambda page: ft.Text("404 Not Found"))
       self.page.add(view(self.page))
       self.page.update()