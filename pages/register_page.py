import flet as ft
from components.register_form import RegisterForm


class RegisterPage:
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.register_form = RegisterForm(self.page)

    def build(self):
        return ft.Container(
            content=self.register_form.build(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=20, vertical=20),
        )