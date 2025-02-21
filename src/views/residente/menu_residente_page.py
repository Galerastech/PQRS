import flet as ft

from src.components.residentes.menu_resident_component import Formato_Menu_residentes

class MenuPageResidente(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Formato_Menu_residentes(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )