import flet as ft
from styles.text_colors import color as colores
from typing import Optional, Callable


class Formato_Menu_residentes(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.change_color = change_color

        self.peticion = create_card("P", "PETICION",
                                    'Requerimiento formal y respetuoso dirigido a la administración',
                                    colores.PRIMARY.value, colores.SECONDARY.value, height=500,
                                    on_hover=self.change_color)

        self.queja = create_card("Q", "QUEJA", "Inconformidad que involucra otro(s) residente(s)",
                                    colores.PRIMARY.value, colores.SECONDARY.value)

        self.reclamo = create_card("R", "RECLAMO", "Inconformidad dirigida a la administración",
                                     colores.CONTENT.value, colores.MENU_SECOND.value)

        self.sugerencia = create_card("S", "SUGERENCIA", "Aporte constructivo para la mejora o o felicitaciones para la administración", colores.CONTENT.value,
                                 colores.MENU_SECOND.value)

        self.contenedor1 = ft.Container(
            col=6,
            content=
            ft.Container(
                content=self.peticion
            ),
        )

        self.contenedor2 = ft.Container(
            col=6,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=self.queja
                    ),
                    ft.GridView(
                        semantic_child_count=2,
                        spacing=10,
                        max_extent=425,
                        controls=[
                            ft.Container(
                                content=self.reclamo
                            ),
                            ft.Container(
                                content=self.sugerencia
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
                        color=colores.DEFAULT.value, text_align="center"),
                ft.Text("NOMBRE DEL CONDOMINIO", size= 25, weight=ft.FontWeight.BOLD,
                        color=colores.DEFAULT.value, text_align="center"),
                self.contenedor1,
                self.contenedor2
            ]
        )


def change_color(e): #TODO: QUITAR FUNCION Y AGREGAR LA NAVEGACION
    e.control.bgcolor = ft.colors.RED if e.data == "true" else colores.SECONDARY.value
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
                                          icon_color=colores.PRIMARY.value),
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