from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from all_models import User
from database import get_session
from logging_config import logger
from users.services import UserService

router: APIRouter = APIRouter(prefix='/users', tags=['users'])


@router.get('/')
async def get_all_users(session: Session = Depends(get_session)) -> list[User]:
    return await UserService.get_all_users(session)
