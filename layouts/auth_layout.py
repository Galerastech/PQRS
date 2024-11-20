import flet as ft


class AuthLayout:
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Container()

    def update_content(self, new_content):
        self.content.content = new_content
        self.page.update()

    def build(self):
        return ft.Row(
            controls=[
                ft.Card(
                    color=ft.colors.SECONDARY_CONTAINER,
                    content=ft.Row(
                        controls=[
                            # Imagen a la izquierda
                            ft.Image(
                                src="images/loginImage.jpeg",
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
