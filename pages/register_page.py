import flet as ft
from components.register_form import RegisterForm
from services import AuthService


class RegisterPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.auth = AuthService()

    def build(self):
        return ft.Container(
            content=ft.Column([
                RegisterForm(self.auth)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(top=50)
        )
