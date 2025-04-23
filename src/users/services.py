from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from all_models import User
from database import get_session
from logging_config import logger
from users.schemas import UpdatePasswordRequest, UserCreate
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

    @staticmethod
    async def get_user(user_id: int, session: Session = Depends(get_session)) -> User:
        logger.info(f'Get User with ID - {user_id}')
        user: User | None = session.get(User, user_id)
        if not user:
            logger.warning(f'User with ID - {user_id} not found')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with ID - {user_id} not found')
        return user

    @staticmethod
    async def delete_user(user_id: int, session: Session = Depends(get_session)) -> User:
        logger.warning(f'Delete User request')
        logger.info(f'Get User with ID - {user_id}')
        user: User | None = session.get(User, user_id)
        if not user:
            logger.warning(f'User with ID - {user_id} not found')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with ID - {user_id} not found')

        session.delete(user)
        session.commit()
        return user

    @staticmethod
    async def update_user_password(user_id: int, payload: UpdatePasswordRequest, session: Session = Depends(get_session)) -> User:
        logger.info(f'Update password request - {payload.model_dump_json()}')
        logger.info(f'Get User with ID - {user_id}')
        user: User | None = session.get(User, user_id)
        if not user:
            logger.warning(f'User with ID - {user_id} not found')
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with ID - {user_id} not found')

        # validate password hashes
        old_password_hash: str = user.password_hash
        if not UserUtils.validate_password(payload.old_password, old_password_hash):
            logger.warning(f'Wrong Password')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong Password')

        new_password_hash: str = UserUtils.generate_password_hash(payload.new_password)
        user.password_hash = new_password_hash

        session.commit()
        session.refresh(user)
        return user
