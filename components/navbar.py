import flet as ft
from styles.text_colors import color as colores
        
class ResponsiveNavBar(ft.UserControl):
    def __init__(self):
        super().__init__()
        

        self.componentenavbar = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.IconButton(ft.icons.HOME,
                        icon_color=colores.CONTENT.value,
                        icon_size=30,
                        tooltip="Home",
                        # on_click=lambda _: page.go("/home")
                        ),
                        width="50%",
                        alignment=ft.alignment.top_left
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Stack(
                                    controls=[
                                        ft.IconButton(ft.icons.NOTIFICATIONS, 
                                        icon_color=colores.CONTENT.value,
                                        icon_size=30,
                                        ),
                                        ft.Container(
                                            width=10,
                                            height=10,
                                            bgcolor="red",
                                            border_radius=10,
                                            right=5,
                                            top=5,
                                            # visible=self.new_notifications,
                                        ),
                                    ],
                                ),
                                ft.IconButton(ft.icons.LIBRARY_BOOKS_ROUNDED,
                                icon_color=colores.CONTENT.value,
                                icon_size=30,
                                tooltip="Listado de Clientes",
                                # on_click=lambda _: page.go("/listado_clientes")
                                ),
                                ft.IconButton(ft.icons.PERSON,
                                icon_color=colores.CONTENT.value,
                                icon_size=30,
                                tooltip="Crear Registro",
                                # on_click=lambda _: page.go("/registros_diarios")
                                ),
                            ],
                        ),
                        width="50%",
                        alignment=ft.alignment.top_right
                    ),
                ],
                width="100%",
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                #vertical_alignment=ft.CrossAxisAlignment.START
            ),
            width="100%",
            alignment=ft.alignment.top_left,
            bgcolor=colores.BACKGROUND.value,
            padding=10
        )
    
    def build(self):
        return self.componentenavbar