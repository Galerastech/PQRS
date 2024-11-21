import flet as ft
from flet_core import TextSpan, TextStyle
from services import AuthService


class MainPage(ft.UserControl):
    def __init__(self, auth_service: AuthService):
        super().__init__()
        self.auth = auth_service

    def build(self):
        return ft.Text(
            'Algo en el main page'
        )
