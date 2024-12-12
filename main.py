import flet as ft

from router import Router
from services import AuthService


def main(page: ft.Page):
    page.title = "App PQRS"
    page.padding = 0
    page.window_resizable = True
    page.window_width = 1500
    page.window_height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme = ft.Theme(font_family="Poppins Regular")
    page.theme_mode = ft.ThemeMode.LIGHT

    page.fonts = {
        "SF Pro Bold": "fonts/SFProText-Bold.ttf",
        "SF Pro Heavy": "fonts/SFProText-Heavy.ttf",
        "SF Pro HeavyItalic": "fonts/SFProText-HeavyItalic.ttf",
        "SF Pro Light": "fonts/SFProText-Light.ttf",
        "SF Pro Medium": "fonts/SFProText-Medium.ttf",
        "SF Pro Regular": "fonts/SFProText-Regular.ttf",
        "SF Pro Semibold": "fonts/SFProText-Semibold.ttf",
        "SF Pro SemiboldItalic": "fonts/SFProText-SemiboldItalic.ttf",

        "Poppins ThinItalic": "fonts/poppins/Poppins-ThinItalic.ttf",
        "Poppins Thin": "fonts/poppins/Poppins-Thin.ttf",
        "Poppins Semibold": "fonts/poppins/Poppins-Semibold.ttf",
        "Poppins SemiboldItalic": "fonts/poppins/Poppins-SemiboldItalic.ttf",
        "Poppins Regular": "fonts/poppins/Poppins-Regular.ttf",
        "Poppins MediumItalic": "fonts/poppins/Poppins-MediumItalic.ttf",
        "Poppins Medium": "fonts/poppins/Poppins-Medium.ttf",
        "Poppins LightItalic": "fonts/poppins/Poppins-LightItalic.ttf",
        "Poppins Light": "fonts/poppins/Poppins-Light.ttf",
        "Poppins Italic": "fonts/poppins/Poppins-Italic.ttf",
        "Poppins ExtraLightItalic": "fonts/poppins/Poppins-ExtraLightItalic.ttf",
        "Poppins ExtraLight": "fonts/poppins/Poppins-ExtraLight.ttf",
        "Poppins ExtraBold": "fonts/poppins/Poppins-ExtraBold.ttf",
        "Poppins ExtraBoldItalic": "fonts/poppins/Poppins-ExtraBoldItalic.ttf",
        "Poppins BoldItalic": "fonts/poppins/Poppins-BoldItalic.ttf",
        "Poppins Bold": "fonts/poppins/Poppins-Bold.ttf",
        "Poppins BlackItalic": "fonts/poppins/Poppins-BlackItalic.ttf",
        "Poppins Black": "fonts/poppins/Poppins-Black.ttf",
    }


    page.session.set("access_token", None)
    page.session.set("user_role", None)
    page.session.set("router", Router(page, auth_service=AuthService()))

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets")
