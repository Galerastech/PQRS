from dataclasses import dataclass
from typing import Optional


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

    def register_user(self, email: str, username: str, password:str, confirm_passwod:str) ->tuple[bool, str]:
        if not email or not username or not password or not confirm_passwod:
            return False, "Todos los campos son requeridos"