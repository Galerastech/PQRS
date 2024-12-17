import flet as ft

from layouts.base_layout import BaseLayout


class AuthLayout(BaseLayout):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.image = ft.Image(
            src="images/loginImage.jpg",
            fit=ft.ImageFit.COVER,
            expand=2,
            width=768,
            height=540,
            border_radius=ft.border_radius.only(top_left=12, bottom_left=12),
        )
        self.page.on_resize = self.on_resize

    def on_resize(self, e):
        self.image.visible = self.page.width >= 428
        self.page.update()

    def build(self):
        return ft.ResponsiveRow(
            controls=[
                ft.Card(
                    col={"lg": 8},
                    color=ft.colors.PRIMARY_CONTAINER,
                    content=ft.Row(
                        controls=[self.image, self.content],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    width=1200,
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
