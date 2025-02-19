import flet as ft 
from components.administrador.menu_admon_component import Formato_Menu

class MenuPageAdministrador(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Formato_Menu(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )