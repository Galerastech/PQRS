import flet as ft
from datetime import datetime
from styles.text_colors import color as colores


class Form_reg_pqrs(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.peticion = ft.Text(
            #TODO: Crear funcion para traer el nombre desde el menu
            value= "PETICION",
            color= colores.DEFAULT.value
            
        )

        self.fecha_radicacion = datetime.now()

        self.fecha_inicio = ft.Text(
            value= self.fecha_radicacion.strftime("%d-%m-%y"),
            color= colores.DEFAULT.value
        )
        
        self.modalidad = ft.Dropdown(
                #label="",
                hint_text="Tipo de petición",
                options=[
                    ft.dropdown.Option("PETICION"),
                    ft.dropdown.Option("QUEJA"),
                    ft.dropdown.Option("RECLAMO"),
                    ft.dropdown.Option("SUGERENCIA")
                ], 
                autofocus= True,
                width=400,
                border= ft.border.all(0.2, colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                #bgcolor=ft.colors.DEEP_PURPLE_500
            )
            
        self.descripcion = ft.TextField(
                label="Descripcion",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=True,
                width=400,
                height=150,
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
                                self.peticion,
                                self.fecha_inicio,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        self.modalidad,
                        self.descripcion,
                        ft.Container(height=0),
                        ft.ElevatedButton(
                        text="Radicar",
                        width=400,
                        height=50,
                        bgcolor=colores.SECONDARY.value,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        #TODO: add function for on_click=,
                        color=colores.PRIMARY.value
                    ),
                        ft.Text(
                        '¿Quieres ir al ',
                        color=colores.SECONDARY.value,
                        spans=[
                            ft.TextSpan(
                                text="detalle de peticiones?",
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