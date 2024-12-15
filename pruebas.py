import flet as ft
from pages.SuperAdministrador.register_client_page import Registro_clientesForm
from pages.SuperAdministrador.menu import MenuPage
from pages.SuperAdministrador.registro_contratos_page import Registro_contratos_Form
from pages.SuperAdministrador.table_users_page import Users_dataTable
from pages.SuperAdministrador.carga_masiva_page import Carga_masiva_Form
from pages.residentes_pages.menu_page import MenuPageResidente
from layouts.navbar_layout import Navbar_layout
from pages.residentes_pages.peticiones_page import formResidente_page
from pages.residentes_pages.seguimiento_page import Seguimiento_Peticiones

def main(page: ft.Page):
    page.title = "contador de prueba"
    page.scroll = "auto"
    page.alignment = "center"
    page.theme_mode  = "LIGHT"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos 
    page.add(
            #Carga_masiva_Form()
            #Registro_clientesForm()
            #Registro_contratos_Form()
            #Users_dataTable()
            Seguimiento_Peticiones()
        )

ft.app(main)