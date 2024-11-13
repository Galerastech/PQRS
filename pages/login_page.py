import flet as ft

from components import LoginForm
from services import AuthService


class LoginPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.auth_service = AuthService()

    def build(self):
        return ft.Container(
            content=LoginForm(auth_service=self.auth_service),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )
