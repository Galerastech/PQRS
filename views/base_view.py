import flet as ft


class BaseView(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def show_error(self, message: str):
        self.page.show_snack_bar(
            ft.SnackBar(content=ft.Text(message), bgcolor=ft.colors.ERROR)
        )
        self.page.add(ft.Image(src="images/not_found_image.svg"))

    def show_success(self, message: str):
        self.page.show_snack_bar(
            ft.SnackBar(
                content=ft.Text(message),
                bgcolor=ft.colors.PRIMARY,
                behavior=ft.SnackBarBehavior.FLOATING,
            )
        )
