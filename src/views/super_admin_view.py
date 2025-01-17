import flet as ft

from src.views import BaseView


class SuperAdminView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page
        self.page.title = "Super Administración"
        self.content = [ft.Text("Esta es la vista de super administrador")]

    def build(self):
        return ft.Container(
            content=ft.Column(
                self.content,
                expand=True,
            )
        )
