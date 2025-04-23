from fastapi import APIRouter, Depends
from all_models import User
from sqlmodel import Session, select
from database import get_session
from logging_config import logger

router: APIRouter = APIRouter(prefix='/users', tags=['users'])

@router.get('/')
async def get_all_users(session: Session = Depends(get_session)) -> list[User]:
    users: list[User] = session.exec(
        select(User)
    ).all()
    logger.info(f'Found {len(users)} Users')
    return users
