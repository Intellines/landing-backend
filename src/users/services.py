from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from all_models import User
from database import get_session
from logging_config import logger
from users.schemas import UserCreate
from users.utils import UserUtils


class UserService:
    @staticmethod
    async def get_all_users(session: Session = Depends(get_session)) -> list[User]:
        users: list[User] = session.exec(select(User)).all()
        logger.info(f'Found {len(users)} Users')
        return users

    @staticmethod
    async def create_user(user: UserCreate, session: Session = Depends(get_session)) -> User:
        logger.info(f'Create Users - {user.model_dump_json()}')

        # validate username
        user_with_same_username: User | None = session.exec(select(User).where(User.username == user.username)).one_or_none()
        if user_with_same_username:
            logger.warning(f'User with such username exists - {user.username}')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'User with such username exists - {user.username}',
            )

        # validate email
        user_with_same_email: User | None = session.exec(select(User).where(User.email == user.email)).one_or_none()
        if user_with_same_email:
            logger.warning(f'User with such email exists - {user.email}')
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'User with such email exists - {user.email}',
            )

        # generate password hash
        password_hash: str = UserUtils.generate_password_hash(user.password)

        # insert user
        db_user: User = User(username=user.username, email=user.email, password_hash=password_hash)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    async def get_user(user_id: int, session: Session = Depends(get_session)) -> User:
        logger.info(f'Get User with ID - {user_id}')
        user: User | None = session.get(User, user_id)
        if not user:
            logger.warning(f'User with ID - {user_id} not found')
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User with ID - {user_id} not found'
            )
        return user