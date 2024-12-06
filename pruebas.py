import flet as ft
from pages.SuperAdministrador.register_client_page import Registro_clientesForm
from layouts.navbar_layout import Navbar_layout

def main(page: ft.Page):
    page.title = "contador de prueba"
    page.scroll = "auto"
    page.alignment = "center"
    page.theme_mode  = "LIGHT"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos 
    page.add(
            Registro_clientesForm()
        )

ft.app(main)