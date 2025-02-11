import flet as ft
from flet_core import TextStyle
from components.select_date import seleccionar_date
from components.update_files import update_files_function
from styles.text_colors import color as colores
from datetime import datetime


class Radicar_Peticion_Form(ft.UserControl):
    def __init__(self):
        super().__init__()
              
        self.peticion = ft.Dropdown(
            hint_text="Tipo PQRS",
            options=[
                ft.dropdown.Option("Petición"),
                ft.dropdown.Option("Queja"),
                ft.dropdown.Option("Reclamo"),
                ft.dropdown.Option("Sugerencia"),
            ], 
            autofocus= True,
            width=195,
            border= ft.border.all(0.2, colores.SECONDARY.value),
            border_color=colores.SECONDARY.value,
        )
               
        self.descripcion_peticion = ft.TextField(
            label="Deposita aqui tu petición",
            label_style=TextStyle(color=colores.DEFAULT.value),
            border_color=colores.SECONDARY.value,
            width=400,
            #height=400,
            multiline=True,
            autofocus=True,
        )
        
        # self.contacto = ft.TextField(
        #     label="Petición",
        #     label_style=TextStyle(color=ft.colors.BLACK),
        #     border_color=ft.colors.DEEP_PURPLE_500,
        #     width=400,
        #     height=400,
        #     autofocus=True
        # )
        
        self.adjunto = update_files_function("Subir Adjuntos")
        
        self.fecha_actual = datetime.now().strftime("%Y-%m-%d")
        
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
                    "Registro Petición",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                    self.peticion,
                    
                    self.descripcion_peticion,
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
                    self.adjunto,
                    
                    ft.Text(
                    '¿Quieres ir al ',
                    color=ft.colors.DEEP_PURPLE_500,
                    spans=[
                        ft.TextSpan(
                            text="Seguimiento de Peticiones?",
                            style=ft.TextStyle(color=ft.colors.DEEP_PURPLE_500, weight=ft.FontWeight.BOLD),
                            #todo: add function for on_click=lambda e: self.page.go("/register")
                        )
                    ],
                ),
                    ft.Container(height=0, margin=5)
                ],
                
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            bgcolor=ft.colors.GREY_200,
            width=500,
            
        )
        
    def add_peticion():
        # todo: Traer los datos del residente, colocar la fecha que se hace la peticion, y dejar el estado como pendiente de las peticiones
        pass
    