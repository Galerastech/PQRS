import flet as ft
from src.views.administrador.menu_admon_pages import MenuPageAdministrador
from src.views.administrador.normas_admon_pages import Admon_Normas_Page
from src.views.administrador.pqrs_admon_pages import Admon_PQRS_Page
from src.views.administrador.residente_admon_pages import Admon_Residentes_Page

#Residente
from src.views.residente.menu_residente_page import Formato_Menu_residentes
from src.views.residente.peticiones_residente_page import formResidente_page

#SuperAdministrador
from src.views.superadministrador.menu_superadmon_page import Menu_superadmon_Page
from src.views.superadministrador.carga_masiva_page import Carga_masiva_page
from src.views.superadministrador.registro_cliente_page import Registro_cliente_page
from src.views.superadministrador.registro_contratos_page import Registro_Contratos_Page

def main(page: ft.Page):
    page.title = "contador de prueba"
    #page.current_locale = "es"
    page.scroll = "auto"
    page.alignment = "center"
    page.theme_mode  = "LIGHT"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos 
    page.add(
            MenuPageAdministrador()
            )

ft.app(main)