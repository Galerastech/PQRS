import flet as ft
from flet_core import TextStyle
from components.select_date import seleccionar_date
from components.update_files import update_files_function

class Registro_contratos_Form(ft.UserControl):
    def __init__(self):
        super().__init__()
              
        self.modality = ft.Dropdown(
            #label="Tipo de Id",
            hint_text="Modalidad",
            options=[
                ft.dropdown.Option("Arrendamiento"),
                ft.dropdown.Option("Licenciamiento"),
                ft.dropdown.Option("Venta"),
                ft.dropdown.Option("Servicio"),
            ], 
            autofocus= True,
            width=195,
            border= ft.border.all(0.2, ft.colors.DEEP_PURPLE_500),
            border_color=ft.colors.DEEP_PURPLE_500,
            #bgcolor=ft.colors.DEEP_PURPLE_500
            
        )
        
        self.status = ft.Dropdown(
            #label="Tipo de Id",
            hint_text="Estado",
            options=[
                ft.dropdown.Option("Activo"),
                ft.dropdown.Option("Suspendido"),
                ft.dropdown.Option("Finalizado"),
                ft.dropdown.Option("Pendiente"),
            ], 
            autofocus= True,
            width=195,
            border= ft.border.all(0.2, ft.colors.DEEP_PURPLE_500),
            border_color=ft.colors.DEEP_PURPLE_500,
            #bgcolor=ft.colors.DEEP_PURPLE_500
            
        )
        
        self.payment_method = ft.Dropdown(
            #label="Tipo de Id",
            hint_text="Metodo de pago",
            options=[
                ft.dropdown.Option("PSE"),
                ft.dropdown.Option("Efectivo"),
                ft.dropdown.Option("Nequi"),
                ft.dropdown.Option("Daviplata"),
                ft.dropdown.Option("Transferencia")
            ], 
            autofocus= True,
            width=242,
            border= ft.border.all(0.2, ft.colors.DEEP_PURPLE_500),
            border_color=ft.colors.DEEP_PURPLE_500,
            #bgcolor=ft.colors.DEEP_PURPLE_500   
        )
        
        self.identificacion = ft.TextField(
            label="Identificacion",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True,
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        
        self.contacto = ft.TextField(
            label="Nombre del Contacto o responsable",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True
        )
        
        self.nom_conjunto = ft.TextField(
            label="Nombre Conjunto ",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True
        )
               
        self.telefono = ft.TextField(
            label="telefono",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=400,
            autofocus=True,
            input_filter=ft.NumbersOnlyInputFilter(),
        )  
        
        self.start_date = seleccionar_date("Fecha Inicial")
        
        self.end_date = seleccionar_date("Fecha Final")
        
        self.update_files_function = update_files_function("Cargar Contrato")
        
        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )      
        
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                    "Registro Contratos",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                    self.identificacion,
                    self.nom_conjunto,
                    self.contacto,
                    self.telefono,
                    ft.Row(
                        controls=[
                            self.modality,
                            self.status,
                        ],
                        alignment= ft.MainAxisAlignment.CENTER,
                        
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    self.start_date,
                                    self.end_date
                                ],
                                spacing=0,
                                alignment= ft.MainAxisAlignment.CENTER,
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER
                                
                                ),
                            self.payment_method,    
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        
                    ),
                    self.update_files_function,
                    ft.Container(height=0),
                    ft.ElevatedButton(
                    text="Guardar",
                    width=400,
                    height=50,
                    bgcolor='#673ab7',
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(10)),
                    #todo: add function for on_click=,
                    color=ft.colors.WHITE
                ),
                    ft.Text(
                    '¿Quieres ir al ',
                    color=ft.colors.DEEP_PURPLE_500,
                    spans=[
                        ft.TextSpan(
                            text="control de clientes?",
                            style=ft.TextStyle(color=ft.colors.DEEP_PURPLE_500, weight=ft.FontWeight.BOLD),
                            #todo: add function for on_click=lambda e: self.page.go("/register")
                        )
                    ],
                ),
                    ft.Container(height=0, margin=5)
                ],
                
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            bgcolor=ft.colors.GREY_200,
            width=500,
            
        )