import time
from time import sleep
from typing import Optional

import flet as ft
import jwt

from config import settings
from src.models.user import User


class AuthService:
    def __init__(self, page: ft.Page):
        self.page = page
        self._current_user: Optional[User] = None
        self.token = None

    def validate_token(self) -> bool:
        try:
            token = self.page.session.get("token")
            if not token:
                return False

            jwt.decode(token,
                       settings.SECRET_KEY,
                       algorithms=[settings.ALGORITHM],
                       options={
                           'verify_exp': True
                       })
            return True
        except jwt.InvalidTokenError:
            self._clear_session()
            return False
        except Exception as e:
            print(f"Error en la validacion : {e}")
            return False

    def _clear_session(self):
        """
        Limpiar los datos de la session del usuario
        """
        self.page.session.remove('token')
        self.page.session.remove('user_data')

    def _current_user(self) -> Optional[User]:
        if not self.get_user():
            return None
        return self._current_user

    def get_user(self) -> Optional[User]:
        """
        obtener el usuario del token
        """
        if not self.token:
            return None
        if not self.validate_token() :
            return None
        payload = jwt.decode(self.token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_data = payload.get('user_data')
        if user_data:
            self._current_user = User(**user_data)
        return self._current_user

