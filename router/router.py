import flet as ft
from typing import Dict, Any, Callable
from dataclasses import dataclass
from .routes import get_routes
from services.auth_service import AuthService


@dataclass
class RouteInfo:
    view: Callable
    layout: Any = None


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.auth_service = AuthService(self.page)
        self.routes: Dict[str, RouteInfo] = {}
        self.current_layout = None

        # Configurar el manejador de rutas
        self.page.on_route_change = self.handle_route_change
        self.setup_routes()

        # Iniciar en la ruta principal
        self.page.go("/login")

    def setup_routes(self):
        """
        Registra las rutas desde el módulo routes.
        Las rutas deben venir de get_routes() como un diccionario.
        """
        route_configs = get_routes(self.page)
        for route_path, route_info in route_configs.items():
            self.register_route(
                route_path, route_info.get("view"), route_info.get("layout")
            )

    def register_route(self, path: str, view_func: Callable, layout=None):
        """
        Registra una nueva ruta en el router
        """
        self.routes[path] = RouteInfo(view=view_func, layout=layout)

    def handle_route_change(self, e: ft.RouteChangeEvent):
        """
        Maneja los cambios de ruta y actualiza la vista
        """
        try:
            route = self.page.route
            if route in self.routes:
                self.navigate_to_route(route)
            else:
                self.show_404()
        except Exception as ex:
            self.handle_error(ex)

    def navigate_to_route(self, route: str):
        """
        Navega a una ruta específica y actualiza la vista
        """
        # Limpiar la página actual
        self.page.controls.clear()

        route_info = self.routes[route]

        try:
            # Crear la vista
            view = route_info.view()

            # Si hay un layout, usarlo
            if route_info.layout:
                if not self.current_layout or not isinstance(
                    self.current_layout, route_info.layout
                ):
                    self.current_layout = route_info.layout(self.page)
                self.current_layout.content = view
                final_view = self.current_layout
            else:
                final_view = view

            # Añadir la vista a la página
            self.page.controls.append(final_view)
            self.page.update()

        except Exception as ex:
            self.handle_error(ex)

    def show_404(self):
        """
        Muestra una página 404 cuando la ruta no existe
        """
        self.page.controls.clear()
        self.page.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("La página que buscas no existe."),
                        ft.Image(src="images/not_found_image.svg"),
                        ft.ElevatedButton(
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLACK,
                            text="Volver al inicio",
                            on_click=lambda _: self.page.go("/login"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True,
            )
        )
        self.page.update()

    def handle_error(self, error: Exception):
        """
        Maneja errores mostrando un mensaje al usuario
        """
        print(f"Error en el router: {str(error)} {error}")  # Para debugging

        self.page.controls.clear()
        self.page.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Ha ocurrido un error", size=24, color=ft.colors.RED),
                        ft.Text(str(error)),
                        ft.ElevatedButton(
                            text="Reintentar",
                            on_click=lambda _: self.page.go(self.page.route),
                        ),
                    ],
                ),
                alignment=ft.alignment.center,
                expand=True,
            )
        )
        self.page.update()

    def go(self, route: str):
        """
        Navega a una ruta específica
        """
        self.page.go(route)

    def get_current_route(self) -> str:
        """
        Obtiene la ruta actual
        """
        return self.page.route
