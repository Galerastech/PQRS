import flet as ft

from src.components.superadministrador.superadmon_menu import Formato_Menu

class Menu_superadmon_Page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Formato_Menu(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )