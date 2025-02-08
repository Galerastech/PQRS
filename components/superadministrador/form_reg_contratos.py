import flet as ft
from flet_core import TextStyle
from .Contratos.formulario_contratos import Form_reg_contrato
from .Contratos.tabla_contratos import Tabla_Contratos

class Registro_contratos_Form(ft.UserControl):
    def __init__(self, page: ft.Page = None):
        super().__init__()
        self.page = page
        self.current_view = "1"

        self.formulario = Form_reg_contrato()
        self.table = Tabla_Contratos(self.page)    

        self.formulario.visible = True
        self.table.visible = False

        self.btn_registrar = ft.ElevatedButton(
                                color = ft.colors.WHITE,
                                text="Registrar/Actualizar",
                                width=200,
                                bgcolor="#094d3f" if self.current_view == "1" else ft.colors.GREY_400,
                                on_click=lambda e: self.on_change(e, "1"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            )

        self.btn_consultar = ft.ElevatedButton(
                                color = ft.colors.WHITE,
                                text="Consultar",
                                width=200,
                                bgcolor="#094d3f" if self.current_view == "2" else ft.colors.GREY_400,
                                on_click=lambda e: self.on_change(e, "2"),
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            )

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("APP PQRS", size= 70, weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLACK45, text_align=ft.TextAlign.CENTER),
                    ft.Text(
                    "Registro Contratos",
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
                        self.formulario,
                        self.table
                        ]
                )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.GREY_200,
            width="100%",
            padding=10, 
            )

    def on_change(self,e, view):
        self.current_view = view

        self.btn_registrar.bgcolor = "#094d3f" if self.current_view == "1" else ft.colors.GREY_400
        self.btn_consultar.bgcolor = "#094d3f" if self.current_view == "2" else ft.colors.GREY_400
        
        self.formulario.visible = (view == "1")
        self.table.visible = (view == "2")

        self.update()