import flet as ft


class AuthLayout:
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Container()
        self.image = ft.Image(
            src="images/loginImage.jpg",
            fit=ft.ImageFit.COVER,
            width=860,
            height=540,
            border_radius=ft.border_radius.only(top_left=12, bottom_left=12),
        )
        self.page.on_resize = self.on_resize

    def on_resize(self, e):
        self.image.visible = self.page.width >= 428
        self.page.update()

    def update_content(self, new_content):
        self.content.content = new_content
        self.page.update()

    def build(self):
        return ft.ResponsiveRow(
            controls=[
                ft.Card(
                    col={"lg": 8},
                    color=ft.colors.SECONDARY_CONTAINER,
                    content=ft.Row(
                        controls=[
                            self.image,
                            self.content
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    width=1200
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
