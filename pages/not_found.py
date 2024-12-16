import flet as ft
class NotFoundPage(ft.Control):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.controls.clear()
        self.page.update()


    def build(self):
        return ft.Container(
            content=ft.Image(src="images/not_found_image.svg", fit=ft.ImageFit.COVER),
            expand=1,
            alignment=ft.alignment.center,
            padding=ft.padding.symmetric(horizontal=20, vertical=20),
        )