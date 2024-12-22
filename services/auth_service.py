from enum import Enum
import json
from typing import Any, Dict, Optional, Tuple
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
        self.ALGORITHM = settings.ALGORITHM
        self.TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.API_URL = "http://localhost:8001"
        self._sesion_data: Dict[str, Any] = {}

        self._load_session()

    async def login(self, username: str, password: str) -> Tuple[bool, str]:
        """
        Realiza el login del usuario y guarda la sesión
        """
        try:
            payload = {"username": username, "password": password}
            response = await self._make_request("POST", "/auth/login", data=payload)

            if response.status_code != 200:
                return False, response.get("detail")

            data = response.json()
            # {'access_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwidGVuYW50X2lkIjpudWxsLCJyb2xlIjoic3VwZXJhZG1pbmlzdHJhdG9yIiwiZXhwIjoxNzM0ODE0MzE2fQ.Sh_aCUPAGiVkThPfbiwzpblnBqee0lYicd8HUNPvCkI', 'token_type': 'bearer', 'expires_in': 60}

            session_data = {
                "access_token": data.get("access_token"),
            }
            self._save_to_storage(session_data)
            return True, "Inicio de sesión exitoso"
        except Exception as ex:
            print(f"An error occurred: {str(ex)}")
            return False, "Credenciales incorrectas, verifica nuevamente..."

    async def logout(self) -> None:
        """
        Deletes the current user's token from the session storage.
        """
        self.page.session.clear()
        self._delete_stored_session()

    async def _make_request(
        self, method: str, endpoint: str, **kwargs
    ) -> Optional[Dict]:
        url = f"{self.API_URL}{endpoint}"
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.request(method, url, **kwargs)
                response.raise_for_status()
                return response
        except httpx.HTTPStatusError as e:
            print(
                f"Request failed with status code {e.response.status_code}: {e.response.text}"
            )
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def _save_to_storage(self, data: dict):
        """
        Guarda la sesión en el almacenamiento
        """
        self.page.session.set("session_data", json.dumps(data))

    def get_user_role(self) -> Optional[UserRole]:
        try:
            #Get session data as a strin and parse JSON
            session_data = self.page.session.get('session_data')
            if not session_data:
                return None
            
            #parse JSON string to dict
            session_dict = json.loads(session_data)
            token = session_dict.get('access_token')

            if not token:
                return None
            
            #decode token to get user role
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return UserRole(payload.get('role'))
        
        except (json.JSONDecodeError, jwt.InvalidTokenError, ValueError) as e :
            print(f"Error getting user role: {str(e)}")

    def is_authenticated(self) -> bool:
        session_data = self.page.session.get("session_data")
        if not session_data:
            return False
        try:
            session_data = json.loads(session_data)
            jwt.decode(
                session_data.get("token"), self.SECRET_KEY, algorithms=[self.ALGORITHM]
            )
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
            if not stored_session:
                return
            if isinstance(stored_session, str):
                stored_session = json.loads(stored_session)

            if stored_session.get("token"):
                self._session_data = stored_session
            else:
                self._delete_stored_session()
        except Exception as e:
            print(f"Error loading session data :{e}")
            self._delete_stored_session()

    def _delete_stored_session(self):
        if "session_data" in self.page.session:
            self.page.session.remove("session_data")

    def _handle_expired_session(self):
        self.logout()
        self.page.go("/login")
