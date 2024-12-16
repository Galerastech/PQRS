from dataclasses import dataclass
from typing import Any, Optional, Tuple, Union, Dict
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
class TokenSchema:
    access_token: str
    token_type: str
    expires_in: int


class AuthService:
    BASE_URL = "http://localhost:8001"

    def __init__(self):
        self.current_user: Optional[User] = None
        self.token: Optional[TokenSchema] = None

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
        return self._make_request("POST", "/auth/signin", json=payload)

        
    def login_superadministrator(self, email: str, password: str) -> Tuple[bool, Union[Dict, str]]:
        payload = {"email": email, "password": password}
        return self._make_request("POST", "/auth/superuser", json=payload)

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
