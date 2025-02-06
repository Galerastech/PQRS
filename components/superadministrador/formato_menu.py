from typing import Optional, Callable

import flet as ft


class Formato_Menu(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.change_color = change_color

        self.usuarios = create_card("U", "USUARIOS",
                                    'Gestión de la base de datos de Usuarios que arriendan la app en modalidad de "software as a service"',
                                    ft.colors.WHITE, ft.colors.GREEN_800, height=500,
                                    on_hover=self.change_color)

        self.clientes = create_card("C", "CLIENTES", "Gestión de los Contratos suscritos con los usuarios",
                                    ft.colors.WHITE, ft.colors.GREEN_800)

        self.dashboard = create_card("D", "DASHBOARD", "Métricas de uso de la app por parte de los usuarios",
                                     ft.colors.BLACK, ft.colors.AMBER_500)

        self.tools = create_card("T", "TOOLS", "Caja de herramientas para la gestión de la app", ft.colors.BLACK,
                                 ft.colors.AMBER_500)

        self.contenedor1 = ft.Container(
            col=6,
            content=
            ft.Container(
                content=self.usuarios
            ),
        )

        self.contenedor2 = ft.Container(
            col=6,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=self.clientes
                    ),
                    ft.GridView(
                        semantic_child_count=2,
                        spacing=10,
                        max_extent=425,
                        controls=[
                            ft.Container(
                                content=self.dashboard
                            ),
                            ft.Container(
                                content=self.tools
                            ),
                        ]
                    )
                ]
            )

        )

    def build(self):
        return ft.ResponsiveRow(
            controls=[
                ft.Text("APP PQRS", size= 70, weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLACK45, text_align="center"),
                self.contenedor1,
                self.contenedor2
            ]
        )


def change_color(e):
    e.control.bgcolor = ft.colors.RED if e.data == "true" else ft.colors.GREEN_800
    e.control.update()


def create_card(inicial: str, titulo: str, descripcion: str, color_texto, color, height: Optional = None,
                on_hover=None):
    return ft.Container(
        on_hover=on_hover,
        alignment=ft.alignment.center,
        bgcolor=color,
        border_radius=10,
        padding=30,
        # expand= True,
        content=
        ft.Stack(
            controls=[
                ft.Container(
                    height=height,
                    content=ft.IconButton(ft.icons.RADIO_BUTTON_OFF,
                                          icon_size=35,
                                          icon_color=ft.colors.WHITE),
                    alignment=ft.alignment.top_right,
                    margin=0
                ),
                ft.Column(
                    controls=[
                        ft.Text(inicial, size=100, weight=ft.FontWeight.BOLD, color=color_texto),
                        ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color=color_texto),
                        ft.Text(descripcion, size=15, weight=ft.FontWeight.NORMAL, color=color_texto),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.START
                )
            ],
        ),

    )