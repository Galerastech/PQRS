import flet as ft 
from components.superadministrador.form_registro_clientes import Registro_clientesForm

class MenuPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Registro_clientesForm(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )