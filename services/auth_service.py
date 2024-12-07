from dataclasses import dataclass
from typing import Optional, Tuple, Union

import requests


@dataclass
class User:
    tenant_id: Optional[int]
    name: str
    email: str
    phone: Optional[str]
    apartment: int
    role: str


@dataclass
class TokenSchema:
    access_token: str
    token_type: str
    expires_in: int
    user: User


class AuthService:
    def __init__(self):
        self.current_user = None
        self.token = None

    def login(self, email: str, password: str):
        print(email, password)
        # try:
        #     response = requests.post("http://localhost:8001/auth/signup", json={
        #         "email": email,
        #         "password": password,
        #     })
        #     response.raise_for_status()
        #     data = response.json()
        #     print(data)
        #     if "access_token" not in data or "user" not in data:
        #         return False, 'Datos de la respuesta son invalidos'
        #
        #     self.token = TokenSchema(
        #         access_token=data["access_token"],
        #         token_type="Bearer",
        #         expires_in=data["expires_in"],
        #         user=User(
        #             tenant_id=data["user"]["tenant_id"],
        #             name=data["user"]["name"],
        #             email=data["user"]["email"],
        #             phone=data["user"]["phone"],
        #             apartment=data["user"]["apartment"],
        #             role=data["user"]["role"],
        #         )
        #     )
        #     self.current_user = self.token.user
        #
        #     return True, self.token
        # except requests.exceptions.RequestException as e:
        #     return False, str(e)
        # except ValueError as e:
        #     return False, f"Error al procesor los datos de la respuesta: {str(e)}"
        # except KeyError as e:
        #     return False, f"Error faltan datos en la respuesta: {str(e)}"

    def logout(self):
        self.current_user = None

    @property
    def is_authenticated(self) -> bool:
        return self.current_user is not None

    # TODO: Intercambiar interaccion de funciones entre primero validar y luego registrar
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

    def get_tenants(self, _):
        try:
            response = requests.get("http://localhost:8001/tenants/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return []
        except requests.exceptions.RequestException as e:
            return []
