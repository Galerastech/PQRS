import flet as ft
from pages.SuperAdministrador.register_client_page import Registro_clientesForm
from pages.SuperAdministrador.menu import MenuPage
from pages.SuperAdministrador.registro_contratos_page import Registro_contratos_Form
from pages.SuperAdministrador.carga_masiva_page import Carga_masiva_Form
from pages.residentes_pages.menu_page import MenuPageResidente
from pages.residentes_pages.peticiones_page import formResidente_page
from pages.administrador.menu_administrador_page import Formato_Menu
from pages.administrador.normas_admon_pages import Admon_Normas
from pages.administrador.pqrs_admon_pages import Administrador_PQRS
from pages.administrador.residentes_admon_page import Admon_residentes

def main(page: ft.Page):
    page.title = "contador de prueba"
    #page.current_locale = "es"
    page.scroll = "auto"
    page.alignment = "center"
    page.theme_mode  = "LIGHT"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos 
    page.add(
            Formato_Menu()
            )

ft.app(main)