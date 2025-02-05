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

import flet as ft

class Tabla_Clientes(ft.UserControl):
    def __init__(self, page: ft.Page = None):
        super().__init__()

        self.page = page

        self.tabla_clientes = ft.DataTable(
                #expand=True,
                border= ft.border.all(2, color = "#094d3f"),
                border_radius=10,
                column_spacing=30,
                columns=[
                    ft.DataColumn(ft.Text("Identificacion", weight="bold")),
                    ft.DataColumn(ft.Text("Nombre", weight="bold")),
                    ft.DataColumn(ft.Text("+OPC", weight="bold")),
                ]
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
                            self.tabla_clientes
                            ]
                    )
                ]
            ),
        )

    def show_data(self):
        self.tabla_clientes.rows= []
        for cliente in clientes:
            self.tabla_clientes.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(cliente["numero_identificacion"])),
                        ft.DataCell(ft.Text(cliente["nombre_cliente"])),
                        ft.DataCell(ft.IconButton(ft.icons.SEARCH, icon_size=20)),
                    ]
                )
            ),
        self.update()

    

    