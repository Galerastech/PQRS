import flet as ft 

class Seguimiento_Peticiones(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        self.filtro = ft.Dropdown(
            hint_text="Filtrar Por:",
            options=[
                ft.dropdown.Option("Todas"),
                ft.dropdown.Option("Pendientes"),
                ft.dropdown.Option("Resueltas"),
                ft.dropdown.Option("En Proceso"),
            ], 
            #autofocus= True,
            width=195,
            #border= ft.border.all(0.2, ft.colors.DEEP_PURPLE_500),
            #border_color=ft.colors.DEEP_PURPLE_500,
        )

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Seguimiento a PQRS"
                        ),
                    ft.Row(
                        controls=[
                            ft.Icon(
                            ft.icons.FILTER_ALT_OUTLINED
                        ),
                            self.filtro
                        
                            
                        ]
                        
                        
                    )
                ]
            )
        )