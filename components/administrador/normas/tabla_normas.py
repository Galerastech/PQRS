import flet as ft
from components.residente_components.ejemplo_peticiones import normas_convivencia
from styles.text_colors import color as colores


class Tabla_Normas(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

#region tabla
        self.tabla_peticiones = ft.DataTable(
            #expand=True,
            border= ft.border.all(2, color = colores.SECONDARY.value),
            border_radius=10,
            column_spacing=30,
            columns=[                    
                ft.DataColumn(ft.Text("N° Norma", weight="bold")),
                ft.DataColumn(ft.Text("Titulo", weight="bold")),
                ft.DataColumn(ft.Text("Descripcion", weight="bold")),
                ft.DataColumn(ft.Text("+OPC", weight="bold")),
            ]
        )
        self.show_data()

        self.dlg_borrar = ft.AlertDialog(
            modal=True,
            content=ft.Text("¿Seguro que desea borrar la norma?"),
            actions=[
                ft.TextButton("Borrar", on_click=self.confirmar_eliminar_norma),
                ft.TextButton("Cancelar", on_click=self.close_dialog)
            ]
        )
#region build
    def build(self):
        return ft.Column(
            controls=[
                self.tabla_peticiones
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.update()


#region funciones
    def show_data(self):
            self.tabla_peticiones.rows= []
            for key, value in normas_convivencia.items():
                numero_id = key
                self.tabla_peticiones.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(key)),
                            ft.DataCell(ft.Text("Titulo")),
                            ft.DataCell(ft.Text(value)),
                            ft.DataCell(ft.Row(
                                controls=[
                                    ft.IconButton(ft.icons.EDIT_SHARP,
                                        icon_color=colores.DEFAULT.value,
                                        #on_click=lambda e, k = key: self.editar_norma(k)
                                        ),
                                    ft.IconButton(ft.icons.DELETE_SHARP,
                                        icon_color=colores.DEFAULT.value,
                                        on_click=lambda e, k=key: self.open_dialog_borrar(k)
                                            )
                                        ]
                                    )
                                ),
                            ]
                        ),
                    )
                
            self.update()

    def open_dialog_borrar(self, key):
        self.norma_a_borrar = key
        self.page.dialog = self.dlg_borrar
        self.dlg_borrar.open = True
        self.page.update()

    def confirmar_eliminar_norma(self, e):
        if self.norma_a_borrar:
            self.eliminar_norma(self.norma_a_borrar)
        self.close_dialog(e)

    def close_dialog(self, e):
        self.dlg_borrar.open = False
        self.page.update()