import flet as ft

from components import AdminForm


class SuperAdminPage:
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.login_form = AdminForm(self.page)

    def build(self):
        return ft.Container(
            content=self.login_form.build(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=20, vertical=20),
        )
