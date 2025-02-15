import flet as ft
from pages.SuperAdministrador.register_client_page import Registro_clientesForm
from pages.SuperAdministrador.menu import MenuPage
from pages.SuperAdministrador.registro_contratos_page import Registro_contratos_Form
from pages.SuperAdministrador.carga_masiva_page import Carga_masiva_Form
from pages.residentes_pages.menu_page import MenuPageResidente
from layouts.navbar_layout import Navbar_layout
from pages.residentes_pages.peticiones_page import formResidente_page
from components.superadministrador.tabla_clientes import Tabla_Clientes
from components.superadministrador.form_reg_usuario import Form_reg_usuario
from components.residente_components.registro_pqrs.form_registro import Form_reg_pqrs
from components.residente_components.menu_residente import Formato_Menu_residentes
from components.residente_components.seguimiento.tabla_peticiones import Tabla_Peticiones
from components.residente_components.historico.selec_fechas import RangoFechas
from components.navbar import ResponsiveNavBar
from components.administrador.admon_residentes.consulta import Consulta_reg_residentes
from components.administrador.admon_residentes.form_registro_resi import Form_reg_residentes

def main(page: ft.Page):
    page.title = "contador de prueba"
    #page.current_locale = "es"
    page.scroll = "auto"
    page.alignment = "center"
    page.theme_mode  = "LIGHT"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER # alineamos 
    page.add(
            #Formato_Menu_residentes()
            #RangoFechas(page)
            #Tabla_Peticiones(page)
            #Form_reg_pqrs()
            #Carga_masiva_Form(page)
            #Tabla_Clientes(page)
            #Form_reg_usuario(page)
            #Ejemplo(page)
            Consulta_reg_residentes(page)
            
            #ResponsiveNavBar()
            #formResidente_page(page)
            #Registro_clientesForm(page)
            #Registro_contratos_Form(page)
            #Users_dataTable()
            #Seguimiento_Peticiones()
            #MenuPageResidente(page)
            #Navbar_layout(page)
            #MenuPage(page)
        )

ft.app(main)