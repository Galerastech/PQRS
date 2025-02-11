import flet as ft
from components.select_date import seleccionar_date
from components.residente_components.ejemplo_peticiones import peticiones
from styles.text_colors import color as colores


class RangoFechas(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.fecha_inicial = seleccionar_date("Fecha Inicial")
        self.fecha_final = seleccionar_date("Fecha Final")

        self.fecha_inicial_valor = ft.Text(
            value=self.fecha_inicial.selected_date.value,
            color=colores.DEFAULT.value,
        )
        self.fecha_final_valor = ft.Text(
            value=self.fecha_final.selected_date.value,
            color=colores.DEFAULT.value,
        )

        self.tabla_peticiones = ft.DataTable(
            #expand=True,
            border= ft.border.all(2, color = colores.SECONDARY.value),
            border_radius=10,
            column_spacing=30,
            columns=[                    
                ft.DataColumn(ft.Text("Numero Radicacion", weight="bold")),
                ft.DataColumn(ft.Text("Fecha Radicación", weight="bold")),
                ft.DataColumn(ft.Text("Descripcion", weight="bold")),
                ft.DataColumn(ft.Text("+OPC", weight="bold")),
            ]
        )
        self.show_data()

        self.form_fecha_detalles = ft.TextField(
                label="Fecha de Radicación",
                value= "",
                read_only=True,
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                width=400,
                autofocus=True
            )

        self.form_descripcion_detalles = ft.TextField(
            label="Descripcion",
            value="",
            read_only=True,
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.DEFAULT.value,
            multiline=True,
            width=400,
            autofocus=True
        )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            content= ft.Column(
                controls=[
                    self.form_fecha_detalles,
                    self.form_descripcion_detalles,
                ],
                spacing=10,
                scroll="auto",
            ),
            actions=[
                ft.TextButton(
                    text="Aceptar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor=colores.SECONDARY.value,
                        color=colores.PRIMARY.value
                    ),
                    #TODO: HACER FUNCION DE CAMBIAR DE ESTADO A ACEPTADA
                    #on_click=lambda e: self.guardar_datos(e),
                ),
                ft.TextButton(
                    text="Rechazar",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor=colores.SECONDARY.value,
                        color=colores.PRIMARY.value
                    ),
                    on_click=lambda e: self.close_dialog(e),
                )
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

    def build(self):
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.fecha_inicial,
                        self.fecha_final,
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Text(f"Ha seleccionado {self.fecha_inicial.selected_date.value} a {self.fecha_final.selected_date.value}"),
                self.tabla_peticiones
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.update()

    def show_data(self):
            self.tabla_peticiones.rows= []
            for peticion in peticiones:
                numero_id = peticion["numero_radicacion"]
                self.tabla_peticiones.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(peticion["numero_radicacion"])),
                            ft.DataCell(ft.Text(peticion["fecha_radicacion"])),
                            ft.DataCell(ft.Text(peticion["descripcion"])),
                            ft.DataCell(ft.IconButton(
                                ft.icons.SEARCH, 
                                icon_size=20,
                                icon_color=colores.SECONDARY.value,
                                data = numero_id,
                                on_click=lambda e: self.open_dialog(e)
                                ),
                            ),
                        ]
                    )
                ),
            self.update()


    def open_dialog(self, e):
        peticion_id = e.control.data
        print(peticion_id)
        peticion = next((c for c in peticiones if c["numero_radicacion"] == peticion_id), None)
        print(peticion)
        if peticion:
            self.form_fecha_detalles.value = peticion["fecha_radicacion"]
            self.form_descripcion_detalles.value = peticion["descripcion"]

            self.page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            self.page.update()

    def close_dialog(self, _):
        self.dlg_modal.open = False
        self.page.update()