import flet as ft

class Navbar_layout(ft.UserControl):
    def __init__(self, content: ft.UserControl):
        super().__init__()
        self.content = content
        
        def build(self):
            return ft.Container(
        ft.AppBar(
                actions=[                    
                    ft.Container(
                        ft.Text("Conjunto residencial")
                    ),
                    ft.CircleAvatar(
                        foreground_image_src="/icons/icon_web.jpeg"
                    ),
                    ft.PopupMenuButton(
                        items=[
                            ft.PopupMenuItem(
                                text="Formulario de radicación"
                                ),
                            ft.PopupMenuItem(
                                text= "Seguimiento a peticiones"
                            ),
                            ft.PopupMenuItem(
                                text= "Configuración"
                            ),                            
                            ft.PopupMenuItem(
                                text= "Cerrar sesión"
                            ),
                        ]
                    )
                ],
            ),
                ft.Container(content=self.content)
            )