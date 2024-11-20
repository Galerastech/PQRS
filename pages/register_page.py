import flet as ft
from components.register_form import RegisterForm
from services import AuthService


class RegisterPage:
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.register_page = RegisterForm(self.page)

    def build(self):
        return ft.Container(
            content=self.register_page.build(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=20, vertical=20),
        )