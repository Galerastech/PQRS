import flet as ft

from components.login_form import LoginForm
from .base_view import BaseView


class LoginView(BaseView):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page

        self.email_field = ft.TextField(
            label="Email",
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=300,
            content_padding=10,
            autofocus=True,
            keyboard_type=ft.KeyboardType.EMAIL,
        )

        self.password_field = ft.TextField(
            label="Contraseña",
            content_padding=10,
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            password=True,
            can_reveal_password=True,
            width=300,
        )

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(
                    "Iniciar Sesión",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                self.email_field,
                self.password_field,
                ft.ElevatedButton(
                    text="Iniciar sesión",
                    bgcolor="#673ab7",
                    style=ft.ButtonStyle(
                        color=ft.colors.DEEP_PURPLE_500,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    color=ft.colors.WHITE,
                    width=300,
                    height=40,
                    on_click=self.handle_login,
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
                    color=ft.colors.BLACK,
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
    
    async def handle_login(self,_):
        try:
            user_data = {
                "email": self.email_field.value.strip(),
                "password": self.password_field.value,
            }
            message = await self.page.auth_service.login(**user_data)
            print(message)
            
        except Exception as e:
            print(e)
