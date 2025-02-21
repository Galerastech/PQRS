
from ..views import LoginView
#Administrador
from ..views.administrador.menu_admon_pages import MenuPageAdministrador
from ..views.administrador.normas_admon_pages import Admon_Normas_Page
from ..views.administrador.pqrs_admon_pages import Admon_PQRS_Page
from ..views.administrador.residente_admon_pages import Admon_Residentes_Page

#Residente
from ..views.residente.menu_residente_page import Formato_Menu_residentes
from ..views.residente.peticiones_residente_page import formResidente_page

#SuperAdministrador
from ..views.superadministrador.menu_superadmon_page import Menu_superadmon_Page
from ..views.superadministrador.carga_masiva_page import Carga_masiva_page
from ..views.superadministrador.registro_cliente_page import Registro_cliente_page
from ..views.superadministrador.registro_contratos_page import Registro_Contratos_Page

def get_routes(page):
    return {
        "/login": {
            "view": lambda :LoginView(page),
        },
        "/administrador/home":{
            "view": lambda : MenuPageAdministrador()
        },
        "/administrador/normas":{
            "view": lambda : Admon_Normas_Page(page)
        },
        "/administrador/pqrs":{
            "view": lambda : Admon_PQRS_Page(page)
        },
        "/administrador/residentes":{
            "view": lambda : Admon_Residentes_Page(page)
        },
        "/residente/home":{
            "view": lambda : Formato_Menu_residentes()
        },
        "/residente/pqrs":{
            "view": lambda : formResidente_page(page)
        },
        "/superadministrador/home":{
            "view": lambda : Menu_superadmon_Page()
        },
        "/superadministrador/cargamasiva":{
            "view": lambda : Carga_masiva_page(page)
        },
        "/superadministrador/regcliente":{
            "view": lambda : Registro_cliente_page(page)
        },
        "/superadministrador/regcontrato":{
            "view": lambda : Registro_Contratos_Page(page)
        },

      
    }
