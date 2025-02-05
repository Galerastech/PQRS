import flet as ft


class Form_reg_usuario(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.tipo_identificacion = ft.Dropdown(
                #label="Tipo de Id",
                hint_text="Tipo ID",
                options=[
                    ft.dropdown.Option("CC"),
                    ft.dropdown.Option("CE"),
                    ft.dropdown.Option("NIT")
                ], 
                autofocus= True,
                width=150,
                border= ft.border.all(0.2, ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                #bgcolor=ft.colors.DEEP_PURPLE_500
            )
            
        self.identificacion = ft.TextField(
                label="Identificacion",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=240,
                autofocus=True,
                input_filter=ft.NumbersOnlyInputFilter(),
            )
            
        self.cliente = ft.TextField(
                label="Nombre del Cliente",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True
            )
            
        self.nom_administrador = ft.TextField(
                label="Nombre administrador ",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True
            )
            
        self.email = ft.TextField(
                label="Email",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True
            )

        self.telefono = ft.TextField(
                label="telefono",
                label_style=ft.TextStyle(color=ft.colors.BLACK45),
                border_color=ft.colors.BLACK45,
                width=400,
                autofocus=True,
                input_filter=ft.NumbersOnlyInputFilter(),
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
                            self.tipo_identificacion,
                            self.identificacion,
                            ],
                        alignment = ft.MainAxisAlignment.CENTER,                    
                    ),
                        self.cliente,
                        self.nom_administrador,
                        self.email,
                        self.telefono,
                        ft.Container(height=0),
                        ft.ElevatedButton(
                        text="Guardar",
                        width=400,
                        height=50,
                        bgcolor="#094d3f",
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                        #todo: add function for on_click=,
                        color=ft.colors.WHITE
                    ),
                        ft.Text(
                        '¿Quieres ir al ',
                        color="#094d3f",
                        spans=[
                            ft.TextSpan(
                                text="listado de clientes?",
                                style=ft.TextStyle(color="#094d3f", weight=ft.FontWeight.BOLD),
                                #todo: add function for on_click=lambda e: self.page.go("/register")
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