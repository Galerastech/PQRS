import flet as ft

from components import LoginForm


class LoginPage:
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.login_form = LoginForm(self.page)

    def build(self):
        return ft.Container(
            content=self.login_form.build(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=20, vertical=20),
        )
