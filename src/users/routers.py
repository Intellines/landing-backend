from fastapi import APIRouter, Depends
from sqlmodel import Session

from all_models import User
from database import get_session
from users.schemas import UserCreate
from users.services import UserService

router: APIRouter = APIRouter(prefix='/users', tags=['users'])


@router.get('/all')
async def get_all_users(session: Session = Depends(get_session)) -> list[User]:
    return await UserService.get_all_users(session)


@router.post('/')
async def create_user(user: UserCreate, session: Session = Depends(get_session)) -> User:
    return await UserService.create_user(user, session)

@router.get('/')
async def get_user(user_id: int, session: Session = Depends(get_session)) -> User:
    return await UserService.get_user(user_id, session)
