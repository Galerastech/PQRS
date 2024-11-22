import flet as ft


class AuthLayout:
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Container()
        self.image = ft.Image(
            src="images/loginImage.jpg",
            fit=ft.ImageFit.COVER,
            width=840,
            height=480,
            border_radius=ft.border_radius.only(top_left=12, bottom_left=12),
            expand=2
        )
        self.page.on_resize = self.on_resize

    def on_resize(self, e):
        self.image.visible = self.page.width >= 600
        self.page.update()

    def update_content(self, new_content):
        self.content.content = new_content
        self.page.update()

    def build(self):
        return ft.ResponsiveRow(
            controls=[
                ft.Card(
                    color=ft.colors.SECONDARY_CONTAINER,
                    content=ft.Row(
                        controls=[
                            self.image,
                            self.content
                        ],
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
