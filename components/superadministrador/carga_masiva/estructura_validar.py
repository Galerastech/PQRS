import flet as ft
from components.update_files import update_files_function
from styles.text_colors import color as colores


class Estructura_Validar(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.identificacion = ft.TextField(
                label="Identificacion",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                width=400,
                autofocus=True,
                input_filter=ft.NumbersOnlyInputFilter(),
            )

        self.nom_conjunto = ft.TextField(
                label="Nombre Conjunto ",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                width=400,
                autofocus=True
            )

        self.dowload_validation = ft.ElevatedButton(
                icon=ft.icons.DOWNLOAD,
                text="Descargar Plantilla",
                width=200,
                height=50,
                bgcolor=colores.SECONDARY.value,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                color=colores.PRIMARY.value,
                #on_click=lambda e: self.download_validation(e)
            )

        self.importar = update_files_function("Importar Archivo")

        self.formulario =  ft.Column(
                controls=[
                    self.identificacion,
                    self.nom_conjunto,
                    ft.Row(
                        controls=[
                            self.dowload_validation,
                            self.importar
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.ElevatedButton(
                        text="Validar",
                        width=400,
                        height=50,
                        bgcolor=colores.SECONDARY.value,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        color=colores.PRIMARY.value,
                        on_click=lambda e: self.open_dialog(e)
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )

        self.tabla_detalles = ft.DataTable(
                border= ft.border.all(2, color = colores.SECONDARY.value),
                border_radius=10,
                column_spacing=30,
                columns=[
                    ft.DataColumn(ft.Text("Filas", weight="bold")),
                    ft.DataColumn(ft.Text("Columnas", weight="bold")),
                    ft.DataColumn(ft.Text("Descripción", weight="bold")),
                ]
            )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            content=ft.Column(
                controls=[
                    self.tabla_detalles
                ],
                spacing=10,
                scroll="auto",
                height=450,
            ),
            actions=[
                ft.TextButton(
                    text="Guardar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor=colores.SECONDARY.value,
                        color=colores.PRIMARY.value
                    ),
                    #on_click=lambda e: self.guardar_datos(e),
                ),
                ft.TextButton(
                    text="Cerrar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor=colores.SECONDARY.value,
                        color=colores.PRIMARY.value
                    ),
                    on_click=lambda e: self.close_dialog(e),
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

    def build(self):
        return self.formulario


    def open_dialog(self, e):
        self.tabla_detalles.rows= []
        #TODO: HACER FUNCION PARA TRAER DATOS Y VALIDAR ARCHIVO
        self.tabla_detalles.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("100")),
                    ft.DataCell(ft.Text("20")),
                    ft.DataCell(ft.Text("No Hay errores")),
                ]
            )
        )
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def close_dialog(self, e):
        self.dlg_modal.open = False
        self.page.update()