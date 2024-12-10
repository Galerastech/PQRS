from dataclasses import dataclass
import datetime
import os
from typing import Any, Optional, Tuple, Union, Dict
from passlib.context import CryptContext
from config import settings
import jwt
import requests


@dataclass
class User:
    tenant_id: Optional[int]
    name: str
    email: str
    phone: Optional[str]
    apartment: Optional[int]
    role: str
@dataclass
class TokenResponse:
    sub: int
    role: str
    exp: int

@dataclass
class TokenSchema:
    access_token: str
    token_type: str
    expires_in: int
    user: User
    



class AuthService:
    BASE_URL = "http://localhost:8002/auth"
    bycrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self):
        self.SECRET_KEY = settings.SECRET_KEY
        self.ALGORITHM = settings.ALGORITHM
        self.current_user: Optional[TokenResponse] = None
        self.token: Optional[TokenSchema] = None

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Tuple[bool, Any]:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return True, response.json()
        except requests.exceptions.RequestException as e:
            return False, str(e)

    def login(self, email: str, password: str, role: str) -> Tuple[bool, Any]:
        payload = {"email": email, "password": password, "rol": role}
        success, data = self._make_request("POST", "/signup", json=payload)

        if not success:
            return False, data

        if not data.get("access_token", ""):
            return False, "Error al iniciar sesion, verifica tus credenciales"

        try:
            user_data = data.get("user", {})
            self.token = TokenSchema(
                access_token=data.get("access_token", ""),
                token_type="Bearer",
                expires_in=data.get("expires_in", 0),
                user=User(
                    tenant_id=user_data.get("tenant_id"),
                    name=user_data.get("name", ""),
                    email=user_data.get("email", ""),
                    phone=user_data.get("phone"),
                    apartment=int(user_data.get("apartment")),
                    role=user_data.get("role", ""),
                )
            )
            self.current_user = self.token.user
            return True, self.token
        except (KeyError, TypeError) as e:
            return False, f"Error al procesar los datos de la respuesta: {str(e)}"

    def login_superadministrator(self, email: str, password: str) -> Tuple[bool, Union[Dict, str]]:
        payload = {"email": email, "password": password}
        return self._make_request("POST", "/superuser", json=payload)

    def logout(self) -> None:
        self.current_user = None
        self.token = None

    @property
    def is_authenticated(self) -> bool:
        return self.current_user is not None

    def validate_register_user(self, email: str, username: str, password: str, confirm_password: str) -> Tuple[bool, str]:
        if not all([email, username, password, confirm_password]):
            return False, "Todos los campos son requeridos"

        if password != confirm_password:
            return False, "Las contraseñas no coinciden"

        return self.register_user(email=email, username=username, password=password)

    def register_user(self, **kwargs) -> Tuple[bool, str]:
        success, data = self._make_request("POST", "/signup", json=kwargs)
        if success:
            return True, "Usuario registrado correctamente"
        return False, data.get("detail", "Error al registrar el usuario")

    def get_tenants(self) -> Union[list, str]:
        success, data = self._make_request("GET", "/tenants")
        return data if success else []

    def validate_login_user(self, email: str, password: str, role: str) -> Tuple[bool, Any]:
        if not all([email, password, role]):
            return False, "Todos los campos son requeridos"

        if role in {"superadministrator", "administrator"}:
            return self.login_superadministrator(email=email, password=password)

        return self.login(email=email, password=password, role=role )

    def verify_token(self, token: str):
        print(token)
        
        