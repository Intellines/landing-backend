from typing import Any

from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from user.models import User
from auth.schemas import Token
from auth.utils import AuthUtils
from database import get_session
from logging_config import logger
from user.utils import UserUtils


class AuthService:
    @staticmethod
    async def authenticate_user(username: str, password: str, session: Session = Depends(get_session)) -> Token:
        logger.info(f'Authenticating User - {username}')
        user: User | None = session.exec(select(User).where(User.username == username)).one_or_none()
        if not user:
            logger.warning(f'User with username - {username} not found')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong username or password')
        logger.info(f'Found User - {user.model_dump_json()}')

        if user.is_disabled is True:
            logger.warning(f'User is disabled')
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not authorized')

        if not UserUtils.validate_password(password, user.password_hash):
            logger.warning('Wrong password')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong username or password')

        token: str = await AuthUtils.create_access_token({'sub': user.username})
        return Token(token=token, token_type='bearer')

    @staticmethod
    async def decode_token(token: str) -> dict | None:
        decoded: Any = await AuthUtils.decode_access_token(token)
        return decoded
