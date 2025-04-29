from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt

from config import config


class AuthUtils:
    @staticmethod
    async def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        to_encode: dict[str, Any] = data.copy()
        to_encode.update({'exp': datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES))})
        return jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)

    @staticmethod
    async def decode_access_token(token: str) -> dict[str, Any] | None:
        try:
            return jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        except JWTError:
            return None
