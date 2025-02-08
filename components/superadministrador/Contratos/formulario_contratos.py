import flet as ft
from ...select_date import seleccionar_date

class Form_reg_contrato(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.fecha_inicio = seleccionar_date("Fecha Inicio")
        self.fecha_finalizacion = seleccionar_date("Fecha Finalizacion")

        self.modalidad = ft.Dropdown(
                #label="",
                hint_text="Modalidad",
                options=[
                    ft.dropdown.Option("Anual"),
                    ft.dropdown.Option("Mensual"),
                    ft.dropdown.Option("Trimestral")
                ], 
                autofocus= True,
                width=400,
                border= ft.border.all(0.2, ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                #bgcolor=ft.colors.DEEP_PURPLE_500
            )
        
        self.pago_seleccion = ft.Dropdown(
                #label="Tipo de Id",
                hint_text="Forma de pago",
                options=[
                    ft.dropdown.Option("Anual"),
                    ft.dropdown.Option("Mensual"),
                    ft.dropdown.Option("Trimestral"),
                    ft.dropdown.Option("Semestral")
                ], 
                autofocus= True,
                width=400,
                border= ft.border.all(0.2, ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                #bgcolor=ft.colors.DEEP_PURPLE_500
            )
            
        self.identificacion = ft.TextField(
                label="Identificacion",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True,
                input_filter=ft.NumbersOnlyInputFilter(),
            )
            
        self.cliente = ft.TextField(
                label="Nombre del Cliente",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True
            )

        self.pago_residente = ft.TextField(
                label="telefono",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True,
                input_filter=ft.NumbersOnlyInputFilter(),
            )  
            
        self.error_text = ft.Text(
                color=ft.colors.RED_400,
                size=12,
                text_align=ft.TextAlign.CENTER
            )

        self.formulario = ft.Column(
                    controls=[
                        self.identificacion,            
                        self.cliente,
                        ft.Row(
                            controls=[
                                self.fecha_inicio,
                                self.fecha_finalizacion,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        self.modalidad,
                        self.pago_seleccion,
                        self.pago_residente,
                        ft.Container(height=0),
                        ft.ElevatedButton(
                        text="Guardar",
                        width=400,
                        height=50,
                        bgcolor="#094d3f",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        #TODO: add function for on_click=,
                        color=ft.colors.WHITE
                    ),
                        ft.Text(
                        '¿Quieres ir al ',
                        color="#094d3f",
                        spans=[
                            ft.TextSpan(
                                text="detalle de contratos?",
                                style=ft.TextStyle(color="#094d3f", weight=ft.FontWeight.BOLD),
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