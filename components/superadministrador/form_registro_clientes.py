import flet as ft
from flet_core import TextStyle


class Registro_clientesForm(ft.UserControl):
    def __init__(self):
        super().__init__()
              
        self.tipo_identificacion = ft.Dropdown(
            #label="Tipo de Id",
            hint_text="Tipo ID",
            options=[
                ft.dropdown.Option("CC"),
                ft.dropdown.Option("CE"),
                ft.dropdown.Option("NIT")
            ], 
            autofocus= True,
            width=150,
            border= ft.border.all(0.2, ft.colors.DEEP_PURPLE_500),
            border_color=ft.colors.DEEP_PURPLE_500,
            #bgcolor=ft.colors.DEEP_PURPLE_500
            
        )
        
        
        self.identificacion = ft.TextField(
            label="Identificacion",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=240,
            autofocus=True,
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        
        self.contacto = ft.TextField(
            label="Nombre del Contacto o responsable",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True
        )
        
        self.nom_conjunto = ft.TextField(
            label="Nombre Conjunto ",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True
        )
        
        self.direccion = ft.TextField(
            label="Dirección",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True
        )

        
        self.telefono = ft.TextField(
            label="telefono",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True,
            input_filter=ft.NumbersOnlyInputFilter(),
        )  
        
        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )      
        
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                    "Registro Clientes",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                    ft.Row(
                    controls=[
                        self.tipo_identificacion,
                        self.identificacion
                        ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    
                    ),
                    self.contacto,
                    self.nom_conjunto,
                    self.direccion,
                    self.telefono,
                    ft.Container(height=0),
                    ft.ElevatedButton(
                    text="Guardar",
                    width=400,
                    height=50,
                    bgcolor='#673ab7',
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(10)),
                    #todo: add function for on_click=,
                    color=ft.colors.WHITE
                ),
                    ft.Text(
                    '¿Quieres ir al ',
                    color=ft.colors.DEEP_PURPLE_500,
                    spans=[
                        ft.TextSpan(
                            text="listado de clientes?",
                            style=ft.TextStyle(color=ft.colors.DEEP_PURPLE_500, weight=ft.FontWeight.BOLD),
                            #todo: add function for on_click=lambda e: self.page.go("/register")
                        )
                    ],
                ),
                    ft.Container(height=0, margin=10)
                ],
                
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            bgcolor=ft.colors.GREY_200,
            width=500,
            
        )