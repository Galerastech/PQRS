import flet as ft 
from components.superadministrador.form_reg_contratos import Registro_contratos_Form

class MenuPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Registro_contratos_Form(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )