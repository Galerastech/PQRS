import flet as ft
from flet_core import TextStyle

class Users_dataTable(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        self.search_filed = ft.TextField(
            label="Nombre",
            value="",
            suffix_icon=ft.icons.SEARCH,
            border= ft.InputBorder.UNDERLINE,
            border_color= ft.colors.DEEP_PURPLE_500,
            #todo: add function for on_change
        )
        
        self.data_table = ft.DataTable(
            #expand=True,
            border= ft.border.all(2,color=ft.colors.DEEP_PURPLE_200),
            border_radius=10,
            column_spacing=30,
            show_checkbox_column=True,
            columns=[
                ft.DataColumn(ft.Text("Identificacion", weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Nombre Conjunto", weight="bold")),
                ft.DataColumn(ft.Text("Contacto", weight="bold")),
                ft.DataColumn(ft.Text("Telefono", weight="bold"), numeric=True),
                ft.DataColumn(ft.Text("Fecha Inicial", weight="bold")),
                ft.DataColumn(ft.Text("Fecha Final", weight="bold")),
                ft.DataColumn(ft.Text("Contrato", weight="bold")),
            ]
        )
        
    def build(self):
        return ft.Container(
            bgcolor= ft.colors.GREY_200,
            padding=10,
            col=8,
            content= ft.Column(
                expand=True,
                controls=[
                    ft.Container(
                        content=ft.Row(
                            scroll="auto",
                            controls=[
                                self.search_filed,
                            ]
                        )
                    ),
                    ft.Container(height=0),
                    ft.Column(
                        expand=True,
                        scroll="auto",
                        controls=[
                            ft.ResponsiveRow(
                                adaptive=True,
                                controls=[
                                    self.data_table,
                                ]
                            )
                        ]
                    )
                ]
            )
        )