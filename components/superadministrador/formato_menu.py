import flet as ft 
from flet_core import TextStyle


class Formato_Menu(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        self.registro_clientes = ft.Container(
            content=ft.Column(
                controls=[
                ft.IconButton(ft.icons.NAVIGATE_NEXT,
                        icon_size= 35, 
                        icon_color=ft.colors.BLACK,
                        
                        ),
                ft.Container(
                    content= ft.Icon(ft.icons.PERSON_OUTLINED,
                        size=110,
                        color= ft.colors.BLACK,
                    ),
                    alignment= ft.alignment.center,
                    width="100%",
                    height="100%",
                ),
                ft.Container(height="20"),
                ft.Text("REGISTRO CLIENTES",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Formulario"),
            ],
                spacing=0
            ),
                width=550,
                height=300,
                margin=5,
                padding=30,
                bgcolor=ft.colors.DEEP_PURPLE_500,
                border_radius=1
        )
        
        self.registro_contratos = ft.Container(
            content=ft.Column(
                controls=[
                    
                ft.IconButton(ft.icons.NAVIGATE_NEXT,
                        icon_size= 35, 
                        icon_color=ft.colors.BLACK,
                        ),
                ft.Container(
                    content= ft.Icon(ft.icons.DOCUMENT_SCANNER_OUTLINED,
                                     size=110,
                                     color= ft.colors.BLACK
                                     ),
                    alignment = ft.alignment.center,
                    width = "100%",
                    height = "100%",
                ),
                ft.Container(height="20"),
                ft.Text("REGISTRO CONTRATOS",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Formulario"),
            ],
                spacing=0
            ),
                width=650,
                height=300,
                margin=5,
                padding=30,
                bgcolor=ft.colors.DEEP_PURPLE_500,
                border_radius=1
        )
        
        self.control_clientes = ft.Container(
            content= ft.Column(
                controls=[
                ft.IconButton(ft.icons.NAVIGATE_NEXT,
                            icon_size= 35, 
                            icon_color=ft.colors.BLACK,
                            ),
                ft.Container(
                    content=ft.Icon(ft.icons.CONTROL_CAMERA,
                        size=110,
                        color= ft.colors.BLACK,
                        ),
                    alignment= ft.alignment.center,
                    width="100%",
                    height="100%",
                ),                
                ft.Container(height="20"),
                ft.Text("CONTROL CLIENTES",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Tabla"),
            ],
                spacing=0
            ),
                width=650,
                height=300,
                margin=5,
                padding=30,
                bgcolor=ft.colors.DEEP_PURPLE_500,
                border_radius=1
        )
        
        self.carga_masiva = ft.Container(
            content=ft.Column(
                controls=[
                ft.IconButton(ft.icons.NAVIGATE_NEXT,
                        icon_size= 35, 
                        icon_color=ft.colors.BLACK,
                        ),
                ft.Container(
                    content=ft.Icon(ft.icons.UPLOAD_FILE,
                        size=110,
                        color= ft.colors.BLACK,
                        ),
                    alignment= ft.alignment.center,
                    width="100%",
                    height="100%",
                ),
                
                ft.Container(height="20"),
                ft.Text("CARGA MASIVA DE CLIENTES",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Formulario"),
            ],
                spacing=0
            ),
                width=550,
                height=300,
                margin=5,
                padding=30,
                bgcolor=ft.colors.DEEP_PURPLE_500,
                border_radius=1
        )
        
    def build(self):
        return ft.Container(
            content= ft.Column(
                controls= [
                    ft.Text("CONTROL PQRS",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER),
                    ft.Row(
                        controls= [
                            self.registro_clientes,
                            self.registro_contratos
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.control_clientes,
                            self.carga_masiva
                        ]
                    )
                ],           
                
                alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            ),
         width="100%",
         height="100%",
         alignment=ft.alignment.center,
         padding=ft.Padding(10, 10, 10, 10),
            
        )