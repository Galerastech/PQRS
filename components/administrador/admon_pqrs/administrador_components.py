import flet as ft
from styles.text_colors import color as colores
from flet_core import TextStyle

from .buscarporfecha import RangoFechas_PQRS
from .tabla_pqrs import Tabla_PQRS

class Administrador_PQRS(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.current_view = "2"

        self.consulta = RangoFechas_PQRS(page)
        self.formulario = Tabla_PQRS(page)

        self.consulta.visible = True
        self.formulario.visible = False

        self.btn_registrar = ft.ElevatedButton(
                            color = colores.PRIMARY.value,
                            text="Recientes/Pendientes",
                            width=200,
                            bgcolor=colores.SECONDARY.value if self.current_view == "1" else colores.BLOCKCOLOR.value,
                            on_click=lambda e: self.on_change(e, "1"),
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        )

        self.btn_consultar = ft.ElevatedButton(
                            color = colores.PRIMARY.value,
                            text="Consultar",
                            width=200,
                            bgcolor=colores.SECONDARY.value if self.current_view == "2" else colores.BLOCKCOLOR.value,
                            on_click=lambda e: self.on_change(e, "2"),
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        )
                        
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("APP PQRS", size= 70, weight=ft.FontWeight.BOLD,
                        color=colores.DEFAULT.value, text_align=ft.TextAlign.CENTER),
                    ft.Text(
                    "Nombre Conjunto",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(height=10),
                ft.Container(
                    content = ft.Row(
                        controls = [
                            self.btn_registrar,
                            self.btn_consultar,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=-3, 
                    )
                ),
                ft.Container(height=20),
                ft.Stack(
                     controls=[
                        self.formulario,
                        self.consulta
                        ]
                )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=colores.BACKGROUND.value,
            width="100%",
            padding=10, 
            )

    def on_change(self,e, view):
        self.current_view = view

        self.btn_registrar.bgcolor = colores.SECONDARY.value if self.current_view == "1" else colores.BLOCKCOLOR.value
        self.btn_consultar.bgcolor = colores.SECONDARY.value if self.current_view == "2" else colores.BLOCKCOLOR.value
        
        self.formulario.visible = (view == "1")
        self.consulta.visible = (view == "2")

        self.update()