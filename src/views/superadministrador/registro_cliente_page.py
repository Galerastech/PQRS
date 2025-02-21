import flet as ft

from src.components.superadministrador.clientes.admon_usuarios_component import Registro_clientesForm

class Registro_cliente_page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Registro_clientesForm(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )