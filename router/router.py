from math import e
from os import access
import flet as ft
import jwt
from router.routes import get_routes, protected_routes
from services import AuthService


class Router:
    def __init__(self, page: ft.Page, auth_service: AuthService):
        self.page = page
        self.routes = get_routes(page)
        self.page.on_route_change = self.on_route_change
        self.auth_service = auth_service
        self.protected_routes = protected_routes()
        
        self.navigate("/login")
    def on_route_change(self, e):
        route = self.page.route
        
        if self.check_route(route):
            self.logout()
        else:
            self.navigate(route)
    def navigate(self, route):
        if route in self.routes:
            self.page.controls.clear()
            layout = self.routes[route]["layout"]
            page = self.routes[route]["page"]()

            layout.update_content(page)
            self.page.add(layout.build())
        else:
            self.page.add(ft.Text("404 Not Found"))
        self.page.update()

    def redirect_based_on_role(self, role):
        route_mapping = {
            "superadministrator": "/superadmin-dashboard",
            "administrador": "/administrator-dashboard",
            "residente": "/dashboard",
        }
        
        target_route = route_mapping.get(role,"/404")
        self.navigate(target_route)
        
    def check_route(self, route)->bool:
        if route in ["/login", "/register"]:
            return True
        
        access_token = self.page.session.get("access_token")
        user_role = self.page.session.get("role")
        
        if not access_token or not user_role:
            return False
        try:
            jwt.decode(str(access_token), 
                       self.auth_service.SECRET_KEY, 
                       algorithms=[self.auth_service.ALGORITHM], 
                       options={"verify_exp": True})
            
            if route in self.protected_routes[user_role]:
                required_role = self.protected_routes[user_role]
                return user_role == required_role
            
            return True
        except jwt.ExpiredSignatureError:
            self.logout()
            self.show_expired_session_alert()
            return False
        except jwt.InvalidTokenError:
            self.logout()
            return False
        except Exception as e:
            print(e)
            self.logout()
            return False
       
    
    def logout(self):
        self.page.session.clear()
        self.navigate("/login")
        
    def show_expired_session_alert(self):
        self.page.dialog = ft.AlertDialog(
            title=ft.Text("Sesion expirada"),
            content=ft.Text("Tu sesion ha expirado. Por favor, inicia sesion nuevamente."),
            actions=[
                ft.TextButton("Aceptar", on_click=lambda e: self.navigate("/login"))
            ]
        )
        self.page.dialog.open = True
        self.page.update()
    