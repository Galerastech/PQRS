import flet as ft
from datetime import datetime
from styles.text_colors import color as colores


class Form_reg_residentes(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.torre = ft.Dropdown(
                #label="",
                hint_text="Torre",
                options=[
                    ft.dropdown.Option("Torre 1"),
                    ft.dropdown.Option("Torre 2"),
                    ft.dropdown.Option("Torre 3"),
                    ft.dropdown.Option("Torre 4"),
                    ft.dropdown.Option("Torre 5"),
                    ft.dropdown.Option("Torre 6"),
                ], 
                autofocus= True,
                width=200,
                border= ft.border.all(0.2, colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                #bgcolor=ft.colors.DEEP_PURPLE_500
            )
        
        self.apartamento = ft.TextField(
                label="Apartamento",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=True,
                width=200,
                autofocus=True
            )

        self.nombres_apellidos= ft.TextField(
                label="Nombres y apellidos",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=True,
                width=400,
                autofocus=True
            )

        self.telefono = ft.TextField(
                label="Telefono",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=True,
                width=400,
                autofocus=True
            )
            
        self.correo = ft.TextField(
                label="Correo Electronico",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=True,
                width=400,
                autofocus=True
            )
            
        self.error_text = ft.Text(
                color=ft.colors.RED_400,
                size=12,
                text_align=ft.TextAlign.CENTER
            )

        self.formulario = ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.torre,
                                self.apartamento,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        self.nombres_apellidos,
                        self.telefono,
                        self.correo,
                        ft.Container(height=0),
                        ft.ElevatedButton(
                        text="Grabar",
                        width=400,
                        height=50,
                        bgcolor=colores.SECONDARY.value,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        #TODO: add function for on_click=,
                        color=colores.PRIMARY.value
                    ),
                        ft.Text(
                        '¿Quieres ir a ',
                        color=colores.SECONDARY.value,
                        spans=[
                            ft.TextSpan(
                                text="consulta de residentes?",
                                style=ft.TextStyle(color=colores.SECONDARY.value, weight=ft.FontWeight.BOLD),
                                #TODO: add function for on_click=lambda e: self.page.go("/register")
                            )
                        ],
                    ),
                        ft.Container(height=0, margin=10)
                    ],
                    visible=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                )

    def build(self):
        return self.formulario