from time import sleep

import flet as ft


class LoginView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.on_resize = self.on_resize

        self.image = ft.Image(
            src="images/loginImage.jpg",
            fit=ft.ImageFit.COVER,
            expand=2,
            width=768,
            height=540,
            border_radius=ft.border_radius.only(top_left=12, bottom_left=12),
        )

        self.email_field = ft.TextField(
            label="Email",
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.BLACK,
            width=300,
            text_style=ft.TextStyle(color=ft.colors.BLACK),
            content_padding=10,
            autofocus=True,
            keyboard_type=ft.KeyboardType.EMAIL,
        )

        self.password_field = ft.TextField(
            label="Contraseña",
            content_padding=10,
            text_style=ft.TextStyle(color=ft.colors.BLACK),
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.BLACK,
            password=True,
            can_reveal_password=True,
            width=300,
        )

        self.content = ft.Column(
            controls=[
                ft.Text(
                    "Iniciar Sesión",
                    size=32,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                self.email_field,
                self.password_field,
                ft.ElevatedButton(
                    text="Iniciar sesión",
                    bgcolor=ft.colors.BLACK,
                    style=ft.ButtonStyle(
                        color=ft.colors.DEEP_PURPLE_500,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    color=ft.colors.WHITE,
                    width=300,
                    height=40,
                    on_click='',
                ),
                ft.Container(
                    content=ft.Divider(thickness=2, color=ft.colors.GREY, opacity=0.2),
                    width=300,
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [
                            ft.Image(src=f"/icons/googleIcon.png", height=30, width=30),
                            ft.Text("Iniciar sesión con Google"),
                        ]
                    ),
                    color=ft.colors.WHITE,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    width=300,
                    height=40,
                    on_click=lambda e: print("Login con Google"),
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=320,
        )

        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    ft.Card(
                        col={"lg": 8},
                        color=ft.colors.WHITE,
                        content=ft.Row(
                            controls=[self.image, self.content],
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
