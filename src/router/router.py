from .routes import get_routes
import flet as ft

from ..services.auth import AuthClient


class AppRouter:
    def __init__(self, page: ft.Page, auth: AuthClient):
        self.auth = auth
        self.routes = get_routes(page)
        self.page = page
        self.set_default_navigation()
        self.setup_routes()

    def set_default_navigation(self):
        if not self.auth.is_authenticated(self.page):
            self.page.go('/login')
        else:
            token = self.page.session.get('token')
            role = self.auth.get_user_role(token)
            if role == 'administrator':
                self.page.go("/admin/dashboard")
            elif role == 'superadmin':
                self.page.go("/superadmin/dashboard")
            elif role == 'resident':
                self.page.go("/resident/dashboard")
            else:
                self.page.go('/login')

    def setup_routes(self):
        def route_change(route):
            self.page.views.clear()

            route_info = self.routes.get(route.route)
            if route_info:
                view = route_info.get('view')()
                self.page.views.append(
                    ft.View(
                        route.route,
                        [view],
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                    )
                )
            else:
                self.page.go('/login')
            self.page.update()

        self.page.on_route_change = route_change
        self.page.go(self.page.route)
