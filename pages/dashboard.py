import flet as ft

class Dashboard:
    def __init__(self, page: ft.Page) -> None:
        self.page = page

    def build(self):
        if self.page.session.get("role") != "residente":
            self.page.session.clear()
            self.page.go("/login")
            return ft.AlertDialog("Acceso no autorizado",content=ft.Text("No tienes permiso para acceder a esta pagina.",color="red"),actions=[ft.TextButton("Aceptar",on_click=lambda e: self.page.go("/login"))])
        return ft.Text("Dashboard")
    
    