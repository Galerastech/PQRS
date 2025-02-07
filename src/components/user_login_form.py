from symtable import Function
from typing import List, Any

import flet as ft
from flet_core.types import MainAxisAlignment, CrossAxisAlignment


class LoginForm(ft.Column):
    def __init__(self, spacing: int = None, alignment: MainAxisAlignment = None,
                 horizontal_alignment: CrossAxisAlignment = None, width: int = None, login_action : Any = None):
        super().__init__(spacing=spacing, width=width)
        self.alignment = alignment
        self.horizontal_alignment = horizontal_alignment
        self.width = width
        self.login_action = login_action

        # Campos de entrada
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

        self.login_button = ft.ElevatedButton(
            text="Iniciar sesión",
            bgcolor=ft.colors.BLACK,
            style=ft.ButtonStyle(
                color=ft.colors.DEEP_PURPLE_500,
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            color=ft.colors.WHITE,
            width=300,
            height=40,
            on_click=self.handle_login,
        )

        self.google_login_button = ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Image(src="/icons/googleIcon.png", height=30, width=30),
                    ft.Text("Iniciar sesión con Google"),
                ]
            ),
            color=ft.colors.WHITE,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
            width=300,
            height=40,
            on_click=lambda e: print("Login con Google"),
        )

        self.span = ft.Text('Error: ',
                            [ft.TextSpan('Aqui va un span', style=ft.TextStyle(color=ft.colors.RED))],
                            visible=False)

        self.controls = [
            ft.Text(
                "Iniciar Sesión",
                size=32,
                color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            ),
            self.span,
            self.email_field,
            self.password_field,
            self.login_button,
            ft.Container(
                content=ft.Divider(thickness=2, color=ft.colors.GREY, opacity=0.2),
                width=300,
            ),
            self.google_login_button,
        ]

    def handle_login(self, e):
        """Manejador para el botón 'Iniciar sesión'."""
        email = self.email_field.value
        password = self.password_field.value

        if not email or not password:
            self.span.visible = True
        else:
            self.span.visible = False
        self.page.update()

        response = self.login_action(email,password)

        print(f'response : {response}')
