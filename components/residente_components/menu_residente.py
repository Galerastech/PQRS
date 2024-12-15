import flet as ft

class Formato_Menu_residentes(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        self.peticiones = ft.Container(
            content=ft.Column(
                controls=[
                ft.IconButton(ft.icons.NAVIGATE_NEXT,
                        icon_size= 35, 
                        icon_color=ft.colors.BLACK,
                        
                        ),
                ft.Container(
                    content= ft.Icon(ft.icons.LIST_ALT,
                        size=110,
                        color= ft.colors.BLACK,
                    ),
                    alignment= ft.alignment.center,
                    width="100%",
                    height="100%",
                ),
                ft.Container(height="20"),
                ft.Text("PETICIÓN",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Son solicitudes formales que se hacen a una entidad para que realice alguna acción o gestione un trámite."),
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
        
        self.quejas = ft.Container(
            content=ft.Column(
                controls=[
                    
                ft.IconButton(ft.icons.NAVIGATE_NEXT,
                        icon_size= 35, 
                        icon_color=ft.colors.BLACK,
                        ),
                ft.Container(
                    content= ft.Icon(ft.icons.REPORT_OUTLINED,
                                     size=110,
                                     color= ft.colors.BLACK
                                     ),
                    alignment = ft.alignment.center,
                    width = "100%",
                    height = "100%",
                ),
                ft.Container(height="20"),
                ft.Text("QUEJAS",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Expresan el descontento de una persona frente a un servicio o producto que no cumple con lo esperado."),
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
        
        self.reclamos = ft.Container(
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
                ft.Text("RECLAMOS",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Son solicitudes formales para que se corrija una situación que causa un perjuicio o daño."),
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
        
        self.sugerencias = ft.Container(
            content=ft.Column(
                controls=[
                ft.IconButton(ft.icons.NAVIGATE_NEXT,
                        icon_size= 35, 
                        icon_color=ft.colors.BLACK,
                        ),
                ft.Container(
                    content=ft.Icon(ft.icons.LIGHTBULB_CIRCLE_OUTLINED,
                        size=110,
                        color= ft.colors.BLACK,
                        ),
                    alignment= ft.alignment.center,
                    width="100%",
                    height="100%",
                ),
                
                ft.Container(height="20"),
                ft.Text("SUGERENCIAS",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        text_align= ft.TextAlign.LEFT
                        ),
                ft.Text("Son propuestas para mejorar un servicio o producto"),
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
                    ft.Text("MENU",
                            size=32,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER),
                    ft.Row(
                        controls= [
                            self.peticiones,
                            self.quejas
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.reclamos,
                            self.sugerencias
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