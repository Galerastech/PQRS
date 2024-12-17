import flet as ft
from .base_layout import BaseLayout

class MainLayout(BaseLayout):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Column([
                # Header
                ft.Container(
                    content=ft.Row([
                        ft.Text("Mi Aplicación", size=24, weight=ft.FontWeight.BOLD),
                        ft.IconButton(
                            icon=ft.icons.LOGOUT,
                            tooltip="Cerrar sesión",
                            on_click=self.handle_logout
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    padding=ft.padding.all(16),
                    bgcolor=ft.colors.SURFACE_VARIANT
                ),
                
                # Main content area with navigation
                ft.Row([
                    # Sidebar navigation
                    ft.Container(
                        content=ft.Column([
                            ft.Container(
                                content=ft.TextButton(
                                    text=item["text"],
                                    icon=item["icon"],
                                    on_click=lambda _, route=item["route"]: self.page.go(route)
                                ),
                                padding=ft.padding.symmetric(horizontal=8)
                            ) for item in self.nav_items
                        ]),
                        width=200,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        padding=ft.padding.all(16)
                    ),
                    
                    # Content area
                    ft.Container(
                        content=self.content,
                        expand=True,
                        padding=ft.padding.all(16)
                    )
                ], expand=True)
            ], expand=True)
        )
    
    def handle_logout(self, _):
        # Implementar lógica de logout
        self.page.go("/login")
