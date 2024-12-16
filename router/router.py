import flet as ft
from router.routes import get_routes
from services import AuthService


class Router:
    def __init__(self, page: ft.Page, auth_service: AuthService):
        self.page = page
        self.page.on_route_change = self.on_route_change
        self.routes = get_routes(page)
        self.auth_service = auth_service
        self.auth_service.load_session()
        self.navigate("/")

        if not self.auth_service.is_authenticated:
            self.navigate("/")
        else:
            self.redirect_based_on_role()

    def on_route_change(self, e):
        self.navigate(self.page.route)

    def navigate(self, route):
        if route in self.routes:

            if self.routes[route].get("protected", False) and not self.auth_service.current_user:
                self.navigate("/")
                return
            # else:
            #     self.redirect_based_on_role(self.auth_service.current_user.get('role'))
            if self.routes[route].get("role") and self.auth_service.current_user.get("role") != self.routes[route].get("role"):
                self.navigate("/unauthorized")
                return

            self.page.controls.clear()
            layout = self.routes[route]["layout"]
            page = self.routes[route]["page"]()
            
            print(self.auth_service.current_user)

            layout.update_content(page)
            self.page.views[0].controls.append(layout.build())
            self.page.update()
        else:
            self.navigate("/404")
        self.page.update()

    def redirect_based_on_role(self):
        # print(self.auth_service.current_user.get("role"))
        if not self.auth_service.current_user.get("role"):
            self.navigate("/")
            return
        role = self.auth_service.current_user.get('role')
        if role == 'superadministrator':
            self.navigate("/super-admin-dashboard")
        elif role == 'administrator':
            self.navigate("/administrator-dashboard")
        elif role == 'residente':
            self.navigate("/dashboard")
        else:
            self.navigate("/unauthorized")