import flet as ft

from styles.text_colors import color as colores


class Form_normas(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
            
        self.grupo = ft.TextField(
                label="Grupo",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=False,
                width=400,
                autofocus=True
            )
            
        self.titulo = ft.TextField(
                label="Titulo",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=False,
                width=400,
                autofocus=True
            )

        self.descripcion = ft.TextField(
                label="Descripcion",
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
                        self.grupo,
                        self.titulo,
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
                                text="detalle de normas?",
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