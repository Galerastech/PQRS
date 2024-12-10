import flet as ft
from flet_core import TextStyle
from components.update_files import update_files_function

class Carga_masiva_Form(ft.UserControl):
    def __init__(self):
        super().__init__()
              
        
        self.identificacion = ft.TextField(
            label="Identificacion",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=200,
            autofocus=True,
            input_filter=ft.NumbersOnlyInputFilter(),
        )
                
        self.nom_conjunto = ft.TextField(
            label="Nombre Conjunto ",
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=300,
            autofocus=True
        )
        
        
        self.update_files_function = update_files_function("Cargar Excel")
        
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
                    "CARGA DE RESIDENTES",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                    ft.Text(
                        "Verifique el NIT y el nombre del conjunto residencial antes de cargar los datos",
                        size=14,
                        text_align=ft.TextAlign.CENTER
                        ),
                    ft.Row(
                        alignment = ft.MainAxisAlignment.CENTER,
                        controls=[
                    self.identificacion,
                    self.nom_conjunto,
                        ]
                    ),
                    ft.Container(height=0),
                    ft.Row(
                        controls=[
                            self.update_files_function,
                            ft.Container(
                            content = ft.Column(
                                controls= [
                                    ft.ElevatedButton(
                                    "Descargar Modelo",
                                    color= ft.colors.BLACK,
                                    icon_color= ft.colors.DEEP_PURPLE_500,
                                    bgcolor= ft.colors.DEEP_PURPLE_100,
                                    icon=ft.icons.DOWNLOAD_OUTLINED,
                                    # on_click=pick_files,
                                    ),
                                    
                                    ]
                                ),
                            margin= ft.margin.only(bottom=30)
                            )
                            
                        ],
                        alignment= ft.MainAxisAlignment.CENTER
                    ),
                    ft.ElevatedButton(
                    text="Guardar",
                    width=400,
                    height=50,
                    bgcolor='#673ab7',
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(10)),
                    #todo: add function for on_click=,
                    color=ft.colors.WHITE
                ),
                    ft.Container(height=0, margin=10),
                ],
                
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
            bgcolor=ft.colors.GREY_200,
            width=600,            
        )