import flet as ft

from src.components.superadministrador.contratos.admon_contratos_component import Registro_contratos_Form

class Registro_Contratos_Page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Registro_contratos_Form(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )