import flet as ft

from layouts import AuthLayout
from pages import LoginPage
from pages.register_page import RegisterPage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.on_route_change
        self.auth_layout = AuthLayout(page)

        self.routes = {
            "/login": {"layout": self.auth_layout, "page": LoginPage(page)},
            "/register": {"layout": self.auth_layout, "page": RegisterPage(page)},
        }

        self.navigate("/login")

    def on_route_change(self, e):
        self.navigate(self.page.route)

    def navigate(self, route):
        if route in self.routes:
            self.page.controls.clear()
            layout = self.routes[route]["layout"]
            page = self.routes[route]["page"]

            layout.update_content(page.build())
            self.page.add(layout.build())
        else:
            self.page.controls.clear()
            self.page.add(ft.Text("404 - Page not found"))
        self.page.update()
