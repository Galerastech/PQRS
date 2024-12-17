import asyncio

import flet as ft
import httpx
import requests

from services import AuthService


class LoginForm:

    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_service = AuthService(page)
        self.tenant_container = ft.Column(visible=False)
        self.alert = ft.AlertDialog(
            open=False,
            modal=True,
            actions=[ft.TextButton("Cerrar", on_click=self.close_alert)],
            actions_alignment=ft.MainAxisAlignment.END,
            alignment=ft.alignment.center
        )
        self.roles = {
            "SuperAdministrador": "superadministrator",
            "administrador": "administrator",
            "residente": "resident"
        }

        

        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )

        self.rol = ft.Dropdown(
            dense=True,
            label="Rol",
            options=[
                ft.dropdown.Option( key=key, text=value, alignment=ft.alignment.center) 
                for value, key in self.roles.items()
            ],
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=300,
            autofocus=True,
            content_padding=10,
            on_change=self.handle_role_change
        )

        self.form = ft.Column(
            controls=[
                self.alert,
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
                    bgcolor='#673ab7',
                    style=ft.ButtonStyle(color=ft.colors.DEEP_PURPLE_500, shape=ft.RoundedRectangleBorder(radius=10)),
                    color=ft.colors.WHITE,
                    width=300,
                    height=40,
                    on_click=self.handle_login
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
                    height=40,
                    on_click=lambda e: print("Login con Google")
                ),
                ft.Text(
                    '¿Aún no tienes cuenta? ',
                    color=ft.colors.DEEP_PURPLE_500,
                    spans=[
                        ft.TextSpan(
                            text="Regístrate",
                            style=ft.TextStyle(color=ft.colors.DEEP_PURPLE_500, weight=ft.FontWeight.BOLD),
                            on_click=lambda e: self.page.go("/register")
                        )
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
    def close_alert(self, e):
        self.alert.open = False
        self.page.update()

    def handle_login(self, e):

        user_data = {
            "email": self.email_field.value.strip(),
            "password": self.password_field.value,
            "role": self.rol.value,
            "tenant_id": self.tenant_container.controls[0].value if self.tenant_container.controls else None
        }
        success, message = self.auth_service.validate_login_user(**user_data)
        print(message)
        if success:
            self.alert.title = ft.Text("Inicio de sesion exitoso")
            self.alert.content = ft.Text(f"{message}")
            self.page.go("/dashboard")
            
        else:
            self.alert.title = ft.Text("Error")
            self.alert.content = ft.Text(f"{message}")

    def build(self):
        return self.form

    def handle_role_change(self, e):
        print(e.control.value)
        if e.control.value != "superadministrator":
            asyncio.run(self.load_tenants())
        else:
            self.tenant_container.controls.clear()
            self.tenant_container.visible = False
        self.page.update()

    async def load_tenants(self):
        tenants =  await self.auth_service.get_tenants()
        self.update_tenant_dropdown(tenants)

    def update_tenant_dropdown(self, tenants):
        if tenants:
            tenant_dropdown = ft.Dropdown(
                dense=True,
                label="Seleccione el Edificio",
                options=[ft.dropdown.Option(key=tenant.get("id"),text=tenant.get("name"),alignment=ft.alignment.center) 
                         for tenant in tenants],
                width=300,
                content_padding=10,
                height=40,
            )
            self.tenant_container.controls = [tenant_dropdown]
            self.tenant_container.visible = True

        else:
            self.tenant_container.controls.clear()
            self.tenant_container.visible = False
