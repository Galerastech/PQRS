import flet as ft
from .base_layout import BaseLayout


class MainLayout(BaseLayout):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page
        self.page.appbar = ft.AppBar(
            shadow_color=ft.colors.GREY_500,
            elevation=3,
            bgcolor=ft.colors.WHITE,
            color=ft.colors.BLACK,
            title=ft.Text("PQRS Application"),
            actions=[
                ft.PopupMenuButton(
                    icon=ft.icons.ACCOUNT_CIRCLE,
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item",
                            checked=False,
                            on_click='',
                        ),
                    ]
                ),
            ],
        )

    def build(self):
        # Crear la Barra de Navegacion
        return ft.Container(
            content=ft.Column(
                [
                    self.content,
                ],
                expand=True,
            )
        )

    def handle_logout(self, _):
        # Implementar lógica de logout
        self.page.auth_service.logout()
        self.page.go("/login")
