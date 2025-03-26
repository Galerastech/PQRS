import flet as ft

from src.components.superadministrador.carga_masiva.admon_carga_masiva import Carga_masiva_Form

class Carga_masiva_page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Carga_masiva_Form(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )