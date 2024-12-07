import flet as ft 
from components.superadministrador.form_reg_contratos import Registro_contratos_Form
from components.superadministrador.datatable_users_component import Users_dataTable

class MenuPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=Users_dataTable(),
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )