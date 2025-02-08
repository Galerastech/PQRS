import flet as ft
from components.update_files import update_files_function

resultado = {
    "Total_Registros_a_Importar": 1800,
    "Total_Registros_Importados": 1500,
    "Diferencia_de_registros": 300,
    "Resultado_de_la_Operacion": "70%",
}

class Importar_Archivos(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.identificacion = ft.TextField(
                label="Identificacion",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True,
                input_filter=ft.NumbersOnlyInputFilter(),
            )

        self.nom_conjunto = ft.TextField(
                label="Nombre Conjunto ",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True
            )

        self.importar = update_files_function("Importar Archivo")

        self.formulario_importar =  ft.Column(
                controls=[
                    self.identificacion,
                    self.nom_conjunto,
                    ft.Row(
                        controls=[
                            self.importar
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.ElevatedButton(
                        text="Importar Archivo",
                        width=400,
                        height=50,
                        bgcolor="#094d3f",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        color=ft.colors.WHITE,
                        on_click=lambda e: self.open_dialog(e)
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )

        self.tabla_detalles = ft.DataTable(
                border= ft.border.all(2, color = "#094d3f"),
                border_radius=10,
                column_spacing=30,
                columns=[
                    ft.DataColumn(ft.Text("Item", weight="bold")),
                    ft.DataColumn(ft.Text("Valor", weight="bold")),
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
                        bgcolor="#094d3f",
                        color=ft.colors.WHITE
                    ),
                    #on_click=lambda e: self.guardar_datos(e),
                ),
                ft.TextButton(
                    text="Cerrar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor="#094d3f",
                        color=ft.colors.WHITE
                    ),
                    on_click=lambda e: self.close_dialog(e),
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

    def build(self):
        return self.formulario_importar


    def open_dialog(self, e):
        self.tabla_detalles.rows= []
        #TODO: HACER FUNCION PARA TRAER DATOS Y VALIDAR ARCHIVO
        if resultado:
            self.tabla_detalles.rows = []
            for key, value in resultado.items():
                self.tabla_detalles.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(f"{key.replace('_', ' ').title()}")),
                            ft.DataCell(ft.Text(str(value))),
                        ]
                    )
                )
        self.page.dialog = self.dlg_modal
        self.dlg_modal.open = True
        self.page.update()

    def close_dialog(self, e):
        self.dlg_modal.open = False
        self.page.update()