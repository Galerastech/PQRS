from typing import Optional
import flet as ft
import requests

from config import settings


class AuthClient:
    def __init__(self, api_url: str):
        """
        Inicializa el cliente de autenticacion

        :param secret_key: Llave secreta para la generacion de tokens
        :param token_expiration: tiempo de expiracion de los tokens
        """
        self.api_url = api_url

    def login(self, username: str, password: str) -> Optional[str]:
        """
        Simula un proceso de inicio de session
        :param username : Nombre de usuario
        :param password : Contraseña
        :return token
        """
        try:
            response = requests.post(
                f'{self.api_url}/auth/token',
                data={'username': username, 'password': password}
            )
            if response.status_code == 200:
                token_data = response.json()
                return token_data.get('access_token')
            return None
        except requests.RequestException:
            return None

    def validate_token(self, token: str) -> bool:
        """
        Verifica si el usuario esta autenticado

        :param page: Pagina de Flet
        :return : True si el usuario es autenticado, False en caso contrario
        """
        try:
            response = requests.post(
                f'{self.api_url}/auth/validate',
                headers={"Authorization": f'Bearer {token}'}
            )
            return response.status_code == 200
        except requests.RequestException:
            return False

    def logout(self, page: ft.Page):
        page.go("/login")

    def is_authenticated(self, page: ft.Page) -> bool:
        """
        Verificar si el usuario esta authenticado

        :param page: Pagina de Flet
        :return: Truen si el usuario esta authenticado, False en caso contrario
        """

        token = page.session.get("token")
        return bool(token and self.validate_token(token))

    def get_user_role(self, token: str) -> Optional[str]:
        """
        Obtener el rol de usuario desde el back de fast_api
        :param token: token de acceso
        :return: rol de usuario['resident','administrator','superadmin]
        """
        try:
            response = requests.get(
                f"{self.api_url}/auth/users/me",
                headers={"Authorization": f"Bearer {token}"}
            )
            if response.status_code == 200:
                return response.json().get('role')
            return None
        except requests.RequestException:
            return None
