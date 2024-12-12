import flet as ft

class ResidentLayout:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.content = ft.Container()
    
    def update_content(self, new_content):
        self.content = new_content
        self.page.update()

    def build(self):
        return ft.Container(content=self.content, 
                            expand=1, 
                            padding=ft.padding.symmetric(horizontal=20, vertical=20))