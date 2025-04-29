import asyncio

from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from all_models import User
from database import get_session
from logging_config import logger
from users.utils import UserUtils


class AuthService:
    @staticmethod
    async def authenticate_user(email: str, password: str, session: Session = Depends(get_session)) -> User:
        logger.info(f'Authenticating User - {email}')
        user: User | None = session.exec(select(User).where(User.email == email)).one_or_none()
        if not user:
            logger.warn(f'User with email - {email} not found')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong email or password')

        logger.info(f'Found User - {user.model_dump_json()}')

        if user.is_disabled is True:
            logger.warn(f'User is disabled')
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not authorized')

        if not UserUtils.validate_password(password, user.password_hash):
            logger.warning('Wrong password')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong email or password')

        logger.info('Authenticated')
        return user
