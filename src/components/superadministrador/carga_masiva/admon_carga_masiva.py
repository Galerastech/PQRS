import flet as ft

from flet_core import TextStyle
from styles.text_colors import color as colores 

from .importar_archivos import Importar_Archivos
from .validar_estructura import Estructura_Validar

class Carga_masiva_Form(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.current_view = "1"

        self.formulario1 = Estructura_Validar()
        self.formulario2 = Importar_Archivos()

        self.formulario1.visible = True
        self.formulario2.visible = False

        self.btn_registrar = ft.ElevatedButton(
                                color = colores.PRIMARY.value,
                                text="Estructura/Validar",
                                width=200,
                                bgcolor= colores.SECONDARY.value if self.current_view == "1" else colores.BLOCKCOLOR.value,
                                on_click=lambda e: self.on_change(e, "1"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            )

        self.btn_consultar = ft.ElevatedButton(
                                color = colores.PRIMARY.value,
                                text="Importar",
                                width=200,
                                bgcolor= colores.SECONDARY.value if self.current_view == "2" else colores.BLOCKCOLOR.value,
                                on_click=lambda e: self.on_change(e, "2"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            )

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("APP PQRS", size= 70, weight=ft.FontWeight.BOLD,
                        color= colores.DEFAULT.value, text_align=ft.TextAlign.CENTER),
                    ft.Text(
                    "Administracion de bases de Residentes",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(height=10),
                ft.Container(
                    content = ft.Row(
                        controls = [
                            self.btn_registrar,
                            self.btn_consultar
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=-3, 
                    )
                ),
                ft.Container(height=20),
                ft.Stack(
                     controls=[
                        self.formulario1,
                        self.formulario2
                        ]
                )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=colores.BLOCKCOLOR.value,
            width="100%",
            padding=10, 
            )

    def on_change(self,e, view):
        self.current_view = view

        self.btn_registrar.bgcolor =  colores.SECONDARY.value if self.current_view == "1" else colores.BLOCKCOLOR.value
        self.btn_consultar.bgcolor =  colores.SECONDARY.value if self.current_view == "2" else colores.BLOCKCOLOR.value
        
        self.formulario1.visible = (view == "1")
        self.formulario2.visible = (view == "2")

        self.update()