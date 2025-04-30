# auth/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlmodel import Session, select

from all_models import User
from auth.utils import AuthUtils
from database import get_session
from logging_config import logger

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')


class AuthDependencies:
    @staticmethod
    async def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)) -> User:
        logger.info(token)
        decoded_token = await AuthUtils.decode_access_token(token)
        if decoded_token is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

        username: str | None = decoded_token.get('sub')
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

        user: User | None = session.exec(select(User).where(User.username == username)).one_or_none()
        if user is None or user.is_disabled:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
        return user
