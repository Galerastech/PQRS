import asyncio

import flet as ft
import httpx
import requests

from services import AuthService

from styles.text_colors import color as colores


class LoginForm:
    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_service = AuthService()
        self.tenant_container = ft.Column(visible=False)

        self.email_field = ft.TextField(
            label="Email",
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.SECONDARY.value,
            width=300,
            content_padding=10,
            autofocus=True
        )

        self.password_field = ft.TextField(
            label="Contraseña",
            content_padding=10,
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.SECONDARY.value,
            password=True,
            can_reveal_password=True,
            width=300
        )

        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )

        self.rol = ft.Dropdown(
            label="Rol",
            options=[
                ft.dropdown.Option(
                    'SuperAdministrador',
                    alignment=ft.alignment.center,
                ),
                ft.dropdown.Option(
                    'Administrador',
                    alignment=ft.alignment.center,
                ),
                ft.dropdown.Option(
                    'Residente',
                    alignment=ft.alignment.center,
                ),
            ],
            label_style=ft.TextStyle(color=colores.DEFAULT.value),
            border_color=colores.SECONDARY.value,
            width=300,
            autofocus=True,
            content_padding=10,
            on_change=self.handle_role_change
        )

        self.form = ft.Column(
            controls=[
                ft.AlertDialog(content=self.error_text),
                ft.Text(
                    "Iniciar Sesión",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                self.rol,
                self.tenant_container,
                self.email_field,
                self.password_field,
                self.error_text,
                ft.ElevatedButton(
                    text="Iniciar sesión",
                    bgcolor=colores.SECONDARY.value,
                    style=ft.ButtonStyle(color=colores.SECONDARY.value, shape=ft.RoundedRectangleBorder(radius=10)),
                    color=colores.PRIMARY.value,
                    width=300,
                    height=40,
                    on_click=''
                ),
                ft.Container(
                    content=ft.Divider(thickness=2, color=colores.BLOCKCOLOR.value, opacity=0.2),
                    width=300
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        [ft.Image(src=f"/icons/googleIcon.png", height=30, width=30),
                         ft.Text("Iniciar sesión con Google")]
                    ),
                    color=colores.DEFAULT.value,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    width=300,
                    height=40,
                    on_click=lambda e: print("Login con Google")
                ),
                ft.Text(
                    '¿Aún no tienes cuenta? ',
                    color=colores.SECONDARY.value,
                    spans=[
                        ft.TextSpan(
                            text="Regístrate",
                            style=ft.TextStyle(color=colores.SECONDARY.value, weight=ft.FontWeight.BOLD),
                            on_click=lambda e: self.page.go("/register")
                        )
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def build(self):
        return self.form

    def handle_role_change(self, e):
        if e.control.value != "SuperAdministrador":
            asyncio.run(self.load_tenants())
        else:
            self.tenant_container.controls.clear()
            self.tenant_container.visible = False
        self.page.update()

    async def fetch_tenants(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://localhost:8002/tenants")
                response.raise_for_status()
                tenants = response.json()
                return tenants
        except Exception as e:
            print(e)
            return []

    async def load_tenants(self):
        tenants = await self.fetch_tenants()
        self.update_tenant_dropdown(tenants)

    def update_tenant_dropdown(self, tenants):
        if tenants:

            tenant_dropdown = ft.Dropdown(
                dense=True,
                label="Seleccione el Edificio",
                options=[ft.dropdown.Option(f"{tenant["name"]}", data=tenant["id"]) for tenant in tenants],
                width=300,
                content_padding=10,
                height=40,
            )
            self.tenant_container.controls = [tenant_dropdown]
            self.tenant_container.visible = True

        else:
            self.tenant_container.controls.clear()
            self.tenant_container.visible = False
        self.page.update()
