import flet as ft 
from components.residente_components.seguimiento_components import Seguimiento_Peticiones

class formResidente_page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Seguimiento_Peticiones(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )