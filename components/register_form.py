import flet as ft
from flet_core import TextSpan, TextStyle

from services import AuthService


class RegisterForm(ft.UserControl):
    def __init__(self, auth_service: AuthService):
        super().__init__()
        self.auth_service = auth_service

        self.username_field = ft.TextField(
            label="Usuario",
            width=300,
            border_color=ft.colors.DEEP_PURPLE_500
        )
        self.password_field = ft.TextField(
            label="Contraseña",
            width=300,
            label_style=TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            password=True,
            can_reveal_password=True
        )
        self.confirm_password_field = ft.TextField(
            label="Confirmar Contraseña",
            width=300,
            border_color=ft.colors.DEEP_PURPLE_500,
            password=True,
            can_reveal_password=True
        )
        self.email_field = ft.TextField(
            label="Email",
            width=300,
            border_color=ft.colors.DEEP_PURPLE_500,
        )
        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )

    def handle_register(self,_):
        user_data = {
            "username": self.username_field.value,
            "email": self.email_field.value,
            "password": self.password_field.value,
            "confirm_password": self.confirm_password_field.value,
        }
        success, message = self.auth_service.validate_register_user(**user_data)
        if success:
            self.error_text.value = message
            self.error_text.style = ft.colors.GREEN
            print("Se va para el login")
            # self.page.go("/login")
        else:
            self.error_text.style = ft.colors.RED
            self.error_text.value = message

        self.update()



    def build(self):
        return ft.Column(
            controls=[
                ft.Text(
                    "Sing Up",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                self.username_field,
                self.email_field,
                self.password_field,
                self.confirm_password_field,
                self.error_text,
                ft.ElevatedButton(
                    text="Crear cuenta",
                    width=300,
                    height=50,
                    color=ft.colors.WHITE,
                    bgcolor="#673ab7",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(10)),
                    on_click=self.handle_register
                ),
                ft.Text('¿Ya tienes una cuenta? ',
                        color=ft.colors.DEEP_PURPLE_500,
                        spans=[TextSpan(
                            "Iniciar Sesion",
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.DEEP_PURPLE_500), )
                        ]
                        )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
