import flet as ft


class ErrorView(ft.View):
    def __init__(self, route: str = '/error', title: str = '', message: str = ''):
        super().__init__()
        self.route = route
        self.title = title
        self.message = message

        self.controls.append(
            ft.Column(
                [
                    ft.Text(self.title, size=32, weight=ft.FontWeight.BOLD),
                    ft.Text(self.message, size=32, weight=ft.FontWeight.BOLD),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )
