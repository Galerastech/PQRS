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
        self.alert = ft.AlertDialog()

<<<<<<< HEAD
    def handle_register(self, _):
        user_data = {
            "username": self.username_field.value.strip(),
            "email": self.email_field.value.strip(),
            "password": self.password_field.value,
            "confirm_password": self.confirm_password_field.value,
        }
        success, message = self.auth_service.validate_register_user(**user_data)
        if success:
            self.alert.title = ft.Text(
                "Registro de Usuario Exitoso",
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
            )
            self.alert.content = ft.Text("Usuario registrado correctamente. Serás redirigido al inicio de sesion")
            self.alert.on_dismiss = lambda: self.page.go("/login")
        else:
            self.alert.title = ft.Text(
                "Error en el registro de Usuario",
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
            )
            self.alert.content = ft.Text(
                message
            )
            self.alert.on_dismiss = None

        self.page.dialog = self.alert
        self.alert.open = True
        self.page.update()

=======
>>>>>>> parent of 63d060f (add-register-funcionality)
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
                ft.ElevatedButton(
                    text="Crear cuenta",
                    width=300,
                    height=50,
                    color=ft.colors.WHITE,
                    bgcolor="#673ab7",
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(10)),
                    on_click=self.auth_service.login(self.username_field.value, self.password_field.value)
                ),
                ft.Text('¿Ya tienes una cuenta? ',
                        color=ft.colors.DEEP_PURPLE_500,
                        spans=[TextSpan(
                            "Iniciar Sesion",
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.DEEP_PURPLE_500
                            ),
                            on_click=lambda _: self.page.go("/login")
                        )
                        ]
                        )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
