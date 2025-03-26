import flet as ft

class Navbar_layout(ft.UserControl):
    def __init__(self, content: ft.UserControl):
        super().__init__()
        self.content = content
        
        def build(self):
            return ft.Container(
                content= [
                    ft.AppBar(
                            actions=[                    
                                ft.Container(
                                    ft.Text("Administrador")
                                ),
                                ft.CircleAvatar(
                                    foreground_image_src="/icons/icon_web.jpeg"
                                ),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(text="Registro Clientes"),
                                        ft.PopupMenuItem(
                                            text= "Control Clientes"
                                        ),
                                        ft.PopupMenuItem(
                                            text= "Registro Contratos"
                                        ),
                                        ft.PopupMenuItem(
                                            text= "Carga Masiva Residentes"
                                        ),
                                        
                                        ft.PopupMenuItem(
                                            text= "Logout"
                                        ),
                                    ]
                                )
                            ],
                        ),
                            ft.Container(content=self.content)
                ]
            )