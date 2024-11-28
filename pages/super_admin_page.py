import flet as ft


class SuperAdminPage:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        return  ft.Text("Aqui va el panel del super")
