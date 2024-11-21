
import flet as ft

from router import Router


def main(page: ft.Page):
    page.title = "App PQRS"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_icon = 'assets/icons/icon.png'

    router = Router(page)

    page.on_route_change = lambda e: router.navigate(page.route)

    page.go("/login")


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")