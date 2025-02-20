import flet as ft 
from components.administrador.admon_residentes.admon_residentes_component import Admon_residentes

class Admon_Residentes_Page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Admon_residentes(self.page),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )