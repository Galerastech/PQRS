import flet as ft

from src.components.administrador.normas.admon_normas_component import Admon_Normas

class Admon_Normas_Page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Admon_Normas(self.page),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )