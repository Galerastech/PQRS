from dataclasses import dataclass
from tokenize import Token
from typing import Any, Optional, Tuple, Union, Dict
import requests
import flet as ft


@dataclass
class User:
    tenant_id: Optional[int]
    name: str
    email: str
    phone: Optional[str]
    apartment: Optional[int]
    role: str


@dataclass
class TokenSchema:
    access_token: str
    token_type: str
    expires_in: int


class AuthService:
    BASE_URL = "http://localhost:8001"

    def __init__(self, page: ft.Page):
        self.page = page
        self._current_user: Optional[User] = None
        self.token: Optional[TokenSchema] = None
        self.load_session()

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Tuple[bool, Any]:
        """Helper to handle HTTP requests."""
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return True, response.json()
        except requests.exceptions.RequestException as e:
            return False, str(e)

    def login(self, email: str, password: str, role: str, tenant_id: int) -> Tuple[bool, Any]:
        payload = {"email": email, "password": password, "rol": role, "tenant_id": tenant_id}
        print(payload)
        success,data = self._make_request("POST", "/auth/signin", json=payload)
        print(data)
        if success:
            self.set_session(data)
            return True, "Inicio de sesion exitoso"
        return True, data

        
    def login_superadministrator(self, email: str, password: str) -> Tuple[bool, Union[Dict, str]]:
        payload = {"email": email, "password": password}
        success, data = self._make_request("POST", "/auth/superuser", json=payload)
        if success:
            self.set_session(data)
            return True, "Inicio de sesion exitoso"
        return True, data

    def logout(self) -> None:
        self.page.client_storage.remove("access_token")
        self.page.client_storage.remove("user")
        self.current_user = None
        self.token = None
        
    @property
    def current_user(self) -> Optional[User]:
        return self._current_user 

    @property
    def is_authenticated(self) -> bool:
        return self._current_user is not None

    def validate_register_user(self, email: str, username: str, password: str, confirm_password: str) -> Tuple[bool, str]:
        if not all([email, username, password, confirm_password]):
            return False, "Todos los campos son requeridos"

        if password != confirm_password:
            return False, "Las contraseñas no coinciden"

        return self.register_user(email=email, username=username, password=password)

    def register_user(self, **kwargs) -> Tuple[bool, str]:
        success, data = self._make_request("POST", "/auth/signup", json=kwargs)
        if success:
            return True, "Usuario registrado correctamente"
        return False, data.get("detail", "Error al registrar el usuario")

    async def get_tenants(self) -> Union[list, str]:
        success, data = self._make_request("GET", "/tenants")
        return data if success else []

    def validate_login_user(self, email: str, password: str, role: str, tenant_id: int | None) -> Tuple[bool, Any]:
        if not all([email, password, role]):
            return False, "Todos los campos son requeridos"

        if role in {"superadministrator"}:
            return self.login_superadministrator(email=email, password=password)

        return self.login(email=email, password=password, role=role, tenant_id=tenant_id)
    
    def load_session(self) -> None:
        token_data = self.page.client_storage.get("access_token")
        user_data = self.page.client_storage.get("user")
        
        if token_data and user_data:
            self.token = TokenSchema(token_data, user_data.get("token_type"), user_data.get("expires_in"))
            self._current_user = {**user_data}
            
    def set_session(self, data: dict)->None:
        self.token = TokenSchema(data.get("access_token"), data.get("token_type"), data.get("expires_in"))
        self._current_user = User(**data["user"])
        
        self.page.client_storage.set("access_token", self.token)
        self.page.client_storage.set("user", self._current_user)
        