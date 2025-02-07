from time import sleep

import flet as ft

from src.components.user_login_form import LoginForm
from src.services.api import AuthService
from src.services.auth import AuthClient


class LoginView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_resize = self.on_resize
        self.auth = AuthClient('http://localhost:8001')

        self.image = ft.Image(
            src="images/loginImage.jpg",
            fit=ft.ImageFit.COVER,
            expand=2,
            width=768,
            height=540,
            border_radius=ft.border_radius.only(top_left=12, bottom_left=12),
        )

        # Formulario de inicio de sesión
        self.login_form = LoginForm(
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=320,
            login_action=self.auth.login
        )

        # Controles principales
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    ft.Card(
                        col={"lg": 8},
                        color=ft.colors.WHITE,
                        content=ft.Row(
                            controls=[self.image, self.login_form],
                        ),
                        width=1200,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]

    def on_resize(self, e):
        self.image.visible = self.page.width >= 428
        self.page.update()


