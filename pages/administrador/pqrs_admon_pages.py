import flet as ft 
from components.administrador.admon_pqrs.administrador_components import Administrador_PQRS

class Admon_PQRS_Page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Administrador_PQRS(self.page),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )