from src.services import AuthClient
from .routes import get_routes
import flet as ft


class AppRouter:
    def __init__(self, page: ft.Page, auth: AuthClient):
        self.auth = auth
        self.routes = get_routes(page)
        self.page = page
        self.set_default_navigation()

    def set_default_navigation(self):
        self.page.go('/login')

    def check_session(self):
        token = self.page.session.get('token')
        if token:
            return
        if jwt

    def setup_routes(self):
        route_configs = get_routes(self.page)
        for route_path, route_info in route_configs.items():
            self.register_router(
                route_path, route_info.get("view"),route_info.get('layout')
            )

    def register_router(self, route_path, param, param1):



