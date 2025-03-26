import flet as ft

from flet_core import TextStyle
from datetime import datetime
from styles.text_colors import color as colores

from .components_residents.buscar_por_fechas import RangoFechas
from .components_residents.form_registro_pqrs import Form_reg_pqrs
from .components_residents.tabla_peticiones import Tabla_Peticiones

class Radicar_Peticion_Form(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.current_view = "1"
        
        self.formulario = Form_reg_pqrs(page)
        self.table = Tabla_Peticiones(page)
        self.historico = RangoFechas(page)

        self.formulario.visible = True
        self.table.visible = False
        self.historico.visible = False

        self.btn_registrar = ft.ElevatedButton(
                                color = colores.PRIMARY.value,
                                text="Registrar",
                                width=200,
                                bgcolor=colores.SECONDARY.value if self.current_view == "1" else colores.BLOCKCOLOR.value,
                                on_click=lambda e: self.on_change(e, "1"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            )

        self.btn_consultar = ft.ElevatedButton(
                                color = colores.PRIMARY.value,
                                text="Recientes",
                                width=200,
                                bgcolor=colores.SECONDARY.value if self.current_view == "2" else colores.BLOCKCOLOR.value,
                                on_click=lambda e: self.on_change(e, "2"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            )
        self.btn_consultar_historico = ft.ElevatedButton(
                                color = colores.PRIMARY.value,
                                text="Historico",
                                width=200,
                                bgcolor=colores.SECONDARY.value if self.current_view == "3" else colores.BLOCKCOLOR.value,
                                on_click=lambda e: self.on_change(e, "3"),
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
                            self.btn_consultar_historico
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=-3, 
                    )
                ),
                ft.Container(height=20),
                ft.Stack(
                     controls=[
                        self.formulario,
                        self.table,
                        self.historico
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
        self.btn_consultar_historico.bgcolor = colores.SECONDARY.value if self.current_view == "3" else colores.BLOCKCOLOR.value
        
        self.formulario.visible = (view == "1")
        self.table.visible = (view == "2")
        self.historico.visible = (view == "3")

        self.update()