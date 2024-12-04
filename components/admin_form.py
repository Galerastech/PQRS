import flet as ft

from services import AuthService


class AdminForm:
    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_service = AuthService()

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
                    on_click=self.handle_login
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def build(self):
        return self.form

    def handle_login(self,_):
        self.auth_service.login(self.email_field.value, self.password_field.value)