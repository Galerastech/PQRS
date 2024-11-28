import flet as ft
from router.routes import get_routes


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.on_route_change
        self.routes = get_routes(page)
        self.navigate("/login")

    def on_route_change(self, e):
        self.navigate(self.page.route)

    def navigate(self, route):
        if route in self.routes:
            self.page.controls.clear()
            layout = self.routes[route]["layout"]
            page = self.routes[route]["page"]()

            layout.update_content(page)
            self.page.add(layout.build())
        else:
            # TODO: Crear la pagina de Not Found 404
            self.page.add(ft.Text("404 Not Found"))
        self.page.update()
