import flet as ft

class AuthLayout(ft.UserControl):
    def __init__(self,  content:ft.UserControl):
        super().__init__()
        self.content = content

    def build(self):
        return ft.Row(
            controls=[
                ft.Card(
                    color=ft.colors.SECONDARY_CONTAINER,
                    content=ft.Row(
                        controls=[
                            # Imagen a la izquierda
                            ft.Image(
                                src="images/loginImage.jpg",
                                fit=ft.ImageFit.COVER,
                                width=840,
                                height=600,
                                border_radius=ft.border_radius.only(top_left=12, bottom_left=12),
                            ),

                            self.content
                        ]
                    ),
                    width=1200,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )