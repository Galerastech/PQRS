import asyncio
from datetime import datetime, timedelta, timezone
from enum import Enum
import json
from typing import Optional, Tuple
import flet as ft
import httpx
import jwt
from config import settings


class UserRole(Enum):
    SUPER_ADMIN = "superadministrator"
    ADMIN = "administrator"
    RESIDENT = "residente"


class AuthService:
    def __init__(self, page: ft.Page):
        self.page = page
        self.SECRET_KEY = settings.SECRET_KEY
        self.ALGOTITHM = settings.ALGORITHM
        self.TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.API_URL = "http://localhost:8001"
        self._sesion_data :Dict[str, Any] = {}

        self._load_session()

    async def login(self, username: str, password: str) -> Tuple[bool, str]:
        # -> dict:
        """
        Realiza el login del usuario y giarda la session
        """
        try:
            payload = {"username": username, "password": password}
            response = await self._make_request("POST", "/auth/login", data=payload)
            if not response:
                return False, "Error en la conexion con del servidor"

            if "acces_token" in response:
                token_data = jwt.decode(
                    response.get("access_token"),
                    self.SECRET_KEY,
                    algorithms=[self.ALGORITHM],
                )
                session_data = {
                    "token": token_data
                }
            else:
                return False, response.get("detail")
        except expression as identifier:
            pass

    async def logout(self) -> None:
        """
        Deletes the current user's token from the session storage.
        """
        self.page.session.clear()
        self._delete_stored_session()
        await self.page.session.remove("session_data")

    async def _make_request(
        self, method: str, endpoint: str, **kwargs
    ) -> Optional[dict]:
        """Helper to handle HTTP requests."""
        url = f"{self.API_URL}{endpoint}"
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.request(method, url, **kwargs)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            print(
                f"Request failed with status code {e.response.status_code}: {e.response.text}"
            )
            return response.json().get("detail")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    async def _save_to_storage(self, data: dict):
        """
        Guarda la session en el storage
        """
        await self.page.session.set("session_data", json.dumps(data))

    def get_user_role(self) -> Optional[UserRole]:
        user = self.get_current_user()
        role = user.get("role")
        try:
            return UserRole(role)
        except ValueError as ve:
            print(f"Invalid user role: {role}")
            return None

    def is_authenticated(self) -> bool:
        token = self.page.session.get("token")
        if not token:
            return False
        try:
            jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return True
        except jwt.ExpiredSignatureError:
            self._handle_expired_session()
            return False
        except jwt.InvalidTokenError:
            return False

    def has_role(self, required_role: UserRole) -> bool:
        user_role = self.get_user_role()
        if not user_role:
            return False

        role_hierarchy = {
            UserRole.SUPER_ADMIN: [
                UserRole.SUPER_ADMIN,
                UserRole.ADMIN,
                UserRole.RESIDENT,
            ],
            UserRole.ADMIN: [UserRole.ADMIN, UserRole.RESIDENT],
            UserRole.RESIDENT: [UserRole.RESIDENT],
        }
        return required_role in role_hierarchy.get(user_role, [])

    async def _save_session(self, session_data: dict):
        self.page.session.set("session_data", session_data)
        await self.page.session.set("session_data", json.dumps(session_data))

    def _load_session(self):
        try:
            stored_session = self.page.session.get("session_data")
            if stored_session:
                session_data = json.loads(stored_session)
                self.page.session.update(session_data)
                if not self.is_authenticated():
                    self._delete_stored_session()
        except Exception:
            self._delete_stored_session()

    def _delete_stored_session(self):
        self.page.session.remove("session_data")

    def _create_access_token(self, user_data) -> dict:
        expire_minutes = int(settings.ACCESS_TOKEN_EXPIRE_MINUTES or 60)
        expire = datetime.now() + timedelta(minutes=expire_minutes)
        to_encode = {
            "sub": str(user_data["id"]),
            "email": user_data["email"],
            "role": user_data["role"],
            "tenant_id": user_data["tenant_id"],
            "exp": expire,
        }
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGOTITHM)

    def _handle_expired_session(self):
        self.logout()
        self.page.go("/login")
