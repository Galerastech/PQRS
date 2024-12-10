import flet as ft
from router.routes import get_routes, get_protected_routes
from services import AuthService


class Router:
    def __init__(self, page: ft.Page, auth_service: AuthService):
        self.page = page
        self.routes = get_routes(page)
        self.page.on_route_change = self.on_route_change
        self.protected_routes = get_protected_routes()
        self.auth_service = auth_service
        
        self.navigate("/login")
    
    def check_route(self, route):
        if route == '/login' or route == '/register':
            return True
        if not self.auth_service.current_user:
            return True
        if route in self.protected_routes:
            required_role = self.protected_routes[route]
            user_role = self.auth_service.current_user.get('role')
            return user_role == required_role
        return True
    
    
    def on_route_change(self, e):
        route = self.page.route
        
        if not self.check_route(route):
            if self.auth_service.current_user:
                self.redirect_based_on_role(self.auth_service.current_user.get('role'))
        else:
            self.navigate(route)
        self.navigate(route)

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

    def redirect_based_on_role(self, role):
        if not role:
            self.navigate("/login")
            return
        
        if role == 'superadministrator':
            self.navigate("/super-admin-dashboard")
        elif role == 'administrator':
            self.navigate("/administrator-dashboard")
        elif role == 'resident':
            self.navigate("/resident-dashboard")
        else:
            self.navigate("/404")