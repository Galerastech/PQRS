clientes = [
    {
        "tipo_id": "CC",
        "numero_identificacion": "123456789",
        "nombre_cliente": "Empresa XYZ",
        "nombre_administrador": "Juan Pérez",
        "correo": "contacto@xyz.com",
        "telefono": "3001234567",
        "contrato": {
            "numero_contrato": "CONT-2024-001",
            "vigencia": "2024-12-31",
            "modalidad": "Anual",
            "pago": "Mensual",
            "valor": 1500000,
            "estado": "activo"
        }
    },
    {
        "tipo_id": "NIT",
        "numero_identificacion": "987654321",
        "nombre_cliente": "Compañía ABC",
        "nombre_administrador": "María López",
        "correo": "info@abc.com",
        "telefono": "3009876543",
        "contrato": {
            "numero_contrato": "CONT-2024-002",
            "vigencia": "2024-12-31",
            "modalidad": "Semestral",
            "pago": "Trimestral",
            "valor": 900000,
            "estado": "activo"
        }
    }
]

from turtle import color
import flet as ft
from styles.text_colors import color as colores

class Tabla_Contratos(ft.UserControl):
    def __init__(self, page: ft.Page = None):
        super().__init__()

        self.page = page

        self.tabla_contratos = ft.DataTable(
                #expand=True,
                border= ft.border.all(2, color = colores.SECONDARY.value),
                border_radius=10,
                column_spacing=30,
                columns=[
                    ft.DataColumn(ft.Text("Identificacion", weight="bold")),
                    ft.DataColumn(ft.Text("Nombre", weight="bold")),
                    ft.DataColumn(ft.Text("+OPC", weight="bold")),
                ]
            )

        self.show_data()

        self.tabla_detalles = ft.DataTable(
                     border= ft.border.all(2, color = colores.SECONDARY.value),
                     border_radius=10,
                     column_spacing=30,
                     columns=[
                         ft.DataColumn(ft.Text("ITEM", weight="bold")),
                         ft.DataColumn(ft.Text("DESCRIPCION", weight="bold")),
                     ]
                 )  
        
        self.estados = ft.RadioGroup(
            value="A",
            content=ft.Row([
                ft.Radio(value="A", label="Activo", active_color=colores.SECONDARY.value),
                ft.Radio(value="I", label="Inactivar", active_color=colores.SECONDARY.value),
                ft.Radio(value="AC", label="Actualizar", active_color=colores.SECONDARY.value)
            ]
            )
        )

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            content= ft.Column(
                controls=[
                    self.tabla_detalles,
                    self.estados
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

        self.show_data()

    def build(self):
        return ft.Container(
            border_radius=10,
            content=ft.Column(
                #expand=True,
                scroll="auto",
                controls=[
                    ft.ResponsiveRow(
                        adaptive=True,
                        controls=[
                            self.tabla_contratos
                            ]
                    )
                ]
            ),
        )

    def show_data(self):
        self.tabla_contratos.rows= []
        for cliente in clientes:
            numero_id = cliente["numero_identificacion"]
            self.tabla_contratos.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(cliente["numero_identificacion"])),
                        ft.DataCell(ft.Text(cliente["nombre_cliente"])),
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
        cliente_id = e.control.data
        print(cliente_id)
        cliente = next((c for c in clientes if c["numero_identificacion"] == cliente_id), None)
        print(cliente)
        if cliente:
            self.tabla_detalles.rows = []

            for key, value in cliente.items():
                print(f"columna 1 {key}, columna 2 {value}")
                if key == "contrato" and isinstance(value, dict):
                    for contract_key, contract_value in value.items():
                        self.tabla_detalles.rows.append(
                            ft.DataRow(
                                cells=[
                                    ft.DataCell(ft.Text(f"{contract_key.replace('_', ' ').title()}")),
                                    ft.DataCell(ft.Text(str(contract_value))),
                                ]
                            )
                        )
            self.page.dialog = self.dlg_modal
            self.dlg_modal.open = True
            self.page.update()

    def close_dialog(self, _):
        self.dlg_modal.open = False
        self.page.update()