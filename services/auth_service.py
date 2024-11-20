from dataclasses import dataclass
from typing import Optional, Tuple

import requests


@dataclass
class User:
    email: str
    username: str


class AuthService:
    def __init__(self):
        self.current_user: Optional[User] = None
        # Usuario de prueba
        self._users = {
            "test@test.com": {
                "password": "123456",
                "username": "test_user"
            }
        }

    def login(self, email: str, password: str) -> tuple[bool, str]:
        if not email or not password:
            return False, "Todos los campos son requeridos"

        user_data = self._users.get(email)
        if not user_data:
            return False, "Usuario no encontrado"

        if user_data["password"] != password:
            return False, "Contraseña incorrecta"

        self.current_user = User(
            email=email,
            username=user_data["username"]
        )
        return True, "Login exitoso"

    def logout(self):
        self.current_user = None

    @property
    def is_authenticated(self) -> bool:
        return self.current_user is not None

    def validate_register_user(self, **kwargs, ) -> Tuple[bool, str]:
        email = kwargs.get("email")
        username = kwargs.get("username")
        password = kwargs.get("password")
        confirm_password = kwargs.get("confirm_password")

        if not email or not password or not confirm_password or not username:
            return False, "Todos los campos son requeridos"

        if password != confirm_password:
            return False, "las contraseñas no coinciden"

        success, message = self.register_user(email=email, username=username, password=password)
        return success, message

    def register_user(self, **kwargs) -> Tuple[bool, str]:
        try:
            response = requests.post(
                "http://localhost:8001/auth/signup",
                json=kwargs
            )
            if response.status_code == 200:
                return True, "Usuario registrado correctamente"
            else:
                return False, response.json().get("detail")
        except requests.exceptions.RequestException as e:
            return False, str(e)