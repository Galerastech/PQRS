import asyncio
from os import access

import flet as ft
import httpx
import jwt
import requests

from services import AuthService

class LoginForm:

    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_service = AuthService()
        self.tenant_container = ft.Column(visible=False)
        self.alert = ft.AlertDialog(
            open=False,
            modal=True,
            actions=[ft.TextButton("Cerrar", on_click=self.close_alert)],
            actions_alignment=ft.MainAxisAlignment.END,
            alignment=ft.alignment.center
        )

        self.email_field = ft.TextField(
            label="Email",
            label_style=ft.TextStyle(color=ft.colors.BLACK),
            border_color=ft.colors.DEEP_PURPLE_500,
            width=300,
            content_padding=10,
            autofocus=True
        )

        self.password_field = ft.TextField(
            label="Contraseña",
            content_padding=10,
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

        self.rol = ft.Dropdown(
            dense=True,
            label="Rol",
            options=[
                ft.dropdown.Option(
                    'superadministrator',
                    alignment=ft.alignment.center,
                ),
                ft.dropdown.Option(
                    'administrator',
                    alignment=ft.alignment.center,
                ),
                ft.dropdown.Option(
                    'Residente',
                    alignment=ft.alignment.center,
                ),
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
                        [ft.Image(src="/icons/googleIcon.png", height=30, width=30),
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
        
        
# TODO: Manejar el proceso de inicio de sesión y la decodificación del token JWT (refactorización)

    def handle_login(self, e):
        """
        Maneja el proceso de inicio de sesión y la decodificación del token JWT
        """
        user_data = {
            "email": self.email_field.value,
            "password": self.password_field.value,
            "role": self.rol.value,
            "tenant": int(self.tenant_container.controls[0].value) if self.tenant_container.visible else None
        }
        
        
        success, message = self.auth_service.validate_login_user(**user_data)
        
        if success:
            self.access_token = message.get("access_token")
            try:
                # Decodificar el token con manejo de errores específicos
                payload = jwt.decode(
                    str(self.access_token),
                    self.auth_service.SECRET_KEY,
                    algorithms=[self.auth_service.ALGORITHM],
                    options={
                        "verify_sub": False,  # Deshabilitar verificación del subject
                        "verify_exp": True    # Mantener verificación de expiración
                    }
                )
                print("Token codificado:", self.access_token)
                # print("Token payload:", payload)
                
                # Guardar información relevante en la sesión
                self.page.session.set("access_token", self.access_token)
                self.page.session.set("role", payload.get("role"))
                self.page.session.set("user", payload.get("user_id"))
                self.page.session.set("tenant", payload.get("tenant_id"))
                
                # Mostrar alerta de éxito
                self.alert.title = ft.Text("Inicio de sesión exitoso")
                self.alert.content = ft.Text(message.get("detail", "Iniciando sesión"))
                self.alert.on_dismiss = self.close_alert
                self.alert.open = True
                
                print("Token decodificado:", payload)
                if payload.get("role"):
                    router = self.page.session.get("router")
                    router.redirect_based_on_role(payload["role"])
                    
                else:
                    self.page.go("/login")
            
                # Redireccionar basado en el rol del payload
                # if payload.get("role"):
                #     self.redirect_based_on_role(payload["role"])
                    
            # except jwt.ExpiredSignatureError:
            #     self.show_error_alert("Token expirado. Por favor, inicie sesión nuevamente.")
            # except jwt.InvalidTokenError as e:
            #     self.show_error_alert(f"Token inválido: {str(e)}")
            except Exception as e:
                print(f"Error decodificando token: {str(e)}")
                # self.show_error_alert("Error procesando las credenciales")
        else:
            self.alert.title = ft.Text("Error en el inicio de sesión")
            self.alert.content = ft.Text(message)
            self.alert.on_dismiss = self.close_alert
            self.alert.open = True
        
        self.page.update()

    def build(self):
        return self.form

    def handle_role_change(self, e):
        if e.control.value != "superadministrator":
            asyncio.run(self.load_tenants())
        else:
            self.tenant_container.controls.clear()
            self.tenant_container.visible = False
        self.page.update()

    async def fetch_tenants(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://localhost:8001/tenants")
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
                options=[ft.dropdown.Option(key=str(tenant.get("id")), text=tenant.get("name") ) 
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
        self.page.update()
