from fastapi import Depends
from sqlmodel import Session, select

from all_models import User
from database import get_session
from logging_config import logger

class UserService:

    @staticmethod
    async def get_all_users(session: Session = Depends(get_session)) -> list[User]:
        users: list[User] = session.exec(select(User)).all()
        logger.info(f'Found {len(users)} Users')
        return users