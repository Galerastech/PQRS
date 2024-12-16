import flet as ft

class MainLayout(ft.Control):
    def __init__(self, page: ft.Page):
        self.page = page
        self.content = ft.Container()

    def update_content(self, new_content):
        self.content.content = new_content
        self.page.update()


    def build(self):
        return self.content