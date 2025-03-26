import flet as ft

from datetime import datetime
from styles.text_colors import color as colores

from src.components.dicts_para_ejemplos.residentes import residentes


class Consulta_reg_residentes(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page

        self.torre = ft.Dropdown(
                #label="",
                hint_text="Torre",
                options=[
                    ft.dropdown.Option("Torre 1"),
                    ft.dropdown.Option("Torre 2"),
                    ft.dropdown.Option("Torre 3"),
                    ft.dropdown.Option("Torre 4"),
                    ft.dropdown.Option("Torre 5"),
                    ft.dropdown.Option("Torre 6"),
                ], 
                autofocus= True,
                width=200,
                border= ft.border.all(0.2, colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                #bgcolor=ft.colors.DEEP_PURPLE_500
            )
        
        self.apartamento = ft.TextField(
                label="Apartamento",
                label_style=ft.TextStyle(color=colores.DEFAULT.value),
                border_color=colores.DEFAULT.value,
                multiline=True,
                width=200,
                autofocus=True
            )
    
        self.error_text = ft.Text(
                color=ft.colors.RED_400,
                size=12,
                text_align=ft.TextAlign.CENTER
            )

        self.formulario = ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                self.torre,
                                self.apartamento,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Container(height=0),
                        ft.ElevatedButton(
                        text="Consultar",
                        width=400,
                        height=50,
                        bgcolor=colores.SECONDARY.value,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        #TODO: add function for on_click=,
                        color=colores.PRIMARY.value,
                        on_click=self.search_residente
                    ),
                        ft.Container(height=0, margin=10)
                    ],
                    visible=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                )

        self.tabla_residentes = ft.DataTable(
            border= ft.border.all(2, color = colores.SECONDARY.value),
            border_radius=10,
            column_spacing=30,
            columns=[
                ft.DataColumn(ft.Text("Item", weight="bold")),
                ft.DataColumn(ft.Text("Descripcion", weight="bold")),
            ],
            visible=False,
        )

        self.checkbox_actualizar = ft.Checkbox(
            label="Actualizar", 
            active_color=colores.SECONDARY.value,
            visible=False
            )
            
        self.checkbox_borrar = ft.Checkbox(
            label="Borrar", 
            active_color=colores.SECONDARY.value,
            visible=False
            )
        
        self.botton_continuar = ft.ElevatedButton(
                        text="Continuar",
                        width=400,
                        height=50,
                        bgcolor=colores.SECONDARY.value,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        #TODO: add function for on_click=,y mandar al formulario inicial
                        color=colores.PRIMARY.value,
                        visible=False
                    )

        self.dlg_modal = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Residente No Encontrado", size=14),
                    actions=[
                            ft.TextButton("Cerrar", 
                            style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        bgcolor=ft.colors.RED_500,
                        color=colores.PRIMARY.value
                    ),
                            on_click=lambda e: self.close_dialog(e))
                        ],
                        actions_alignment=ft.MainAxisAlignment.END,
                    )

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    self.formulario,
                    ft.Container(height=20),
                    ft.Column(
                        controls=[
                            self.tabla_residentes,
                            ft.Row(
                                controls=[
                                    self.checkbox_actualizar,
                                    self.checkbox_borrar,
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            self.botton_continuar
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            bgcolor=colores.BACKGROUND.value
        )

    def search_residente(self, e):
        torre = self.torre.value
        apto = self.apartamento.value
        self.tabla_residentes.rows = []
        for _, value in residentes.items():
            if value['torre'] == torre and value['apartamento'] == int(apto):
                for atributo, dato in value.items():
                    self.tabla_residentes.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(f"{atributo.replace('_', ' ').title()}")),
                                ft.DataCell(ft.Text(str(dato))),
                            ]
                        )
                    )
                self.tabla_residentes.visible = True
                self.checkbox_actualizar.visible = True
                self.checkbox_borrar.visible = True
                self.botton_continuar.visible = True
                self.update()

            else:
                self.page.dialog = self.dlg_modal
                self.dlg_modal.open = True
                self.page.update()

    def close_dialog(self, e):
        self.dlg_modal.open = False
        self.page.update()
        