import flet as ft

from services import AuthService


class AdminForm:
    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_service = AuthService()
        self.tenant = ft.Dropdown(
            width=300,
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
            ],
        )
        self.email_field = ft.TextField(
            label="Email",
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=300,
            autofocus=True
        )

        self.password_field = ft.TextField(
            label="Contraseña",
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            password=True,
            can_reveal_password=True,
            width=300
        )

        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )
        self.form = ft.Column(
            controls=[
                ft.Text(
                    "Super User",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                self.tenant,
                self.email_field,
                self.password_field,
                self.error_text,
                ft.ElevatedButton(
                    text="Iniciar sesión",
                    bgcolor='#673ab7',
                    style=ft.ButtonStyle(color=ft.colors.DEEP_PURPLE_500,
                                         shape=ft.RoundedRectangleBorder(radius=10)),
                    color=ft.colors.WHITE,
                    width=300,
                    height=50,
                    on_click=''
                ),
                ft.Container(
                    content=ft.Divider(thickness=2, color=ft.colors.GREY, opacity=0.2),
                    width=300
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [ft.Image(src=f"/icons/googleIcon.png", height=30, width=30),
                         ft.Text("Iniciar sesión con Google")]
                    ),
                    color=ft.colors.BLACK,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    width=300,
                    height=50,
                    on_click=lambda e: print("Login con Google")
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def build(self):
        return self.form
