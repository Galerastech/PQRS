import flet as ft

class SuperAdminLayout:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.content = ft.Container()
    
    def update_content(self, new_content):
        self.content = new_content
        self.page.update()

    def build(self):
        if self.page.session.get("role") != "superadministrator":
            return ft.AlertDialog("Acceso no autorizado",content=ft.Text("No tienes permiso para acceder a esta pagina.",color="red"),actions=[ft.TextButton("Aceptar",on_click=lambda e: self.page.go("/login"))])
        return ft.Container(content=self.content, 
                            expand=1, 
                            padding=ft.padding.symmetric(horizontal=20, vertical=20))