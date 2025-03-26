import flet as ft 
from components.residente_components.form_peticiones import Radicar_Peticion_Form

class formResidente_page(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.radicar = Radicar_Peticion_Form(self.page)

    def build(self):
        return ft.Container(
            content=self.radicar,
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )