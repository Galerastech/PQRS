from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/signin")

def current_tenant(token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        tenant_id = payload.get("tenant_id")
        if tenant_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="No se encontro el tenant en el token"
                                )
        return tenant_id
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Token invalido")