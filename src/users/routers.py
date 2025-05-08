from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from all_models import User
from database import get_session
from users.schemas import UpdateEmailRequest, UpdatePasswordRequest, UpdateUsernameRequest, UserCreate
from users.services import UserService

router: APIRouter = APIRouter(prefix='/users', tags=['users'])


@router.get('/all')
async def get_all_users(session: Session = Depends(get_session)) -> list[User]:
    return await UserService.get_all_users(session)


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, session: Session = Depends(get_session)) -> User:
    return await UserService.create_user(user, session)


@router.get('/byID')
async def get_user_by_id(user_id: int, session: Session = Depends(get_session)) -> User:
    return await UserService.get_user_by_id(user_id, session)


@router.get('/byUsername')
async def get_user_by_username(username: str, session: Session = Depends(get_session)) -> User:
    return await UserService.get_user_by_username(username, session)


@router.delete('')
async def delete_user(user_id: int, session: Session = Depends(get_session)) -> User:
    return await UserService.delete_user(user_id, session)


@router.patch('/updatePassword')
async def update_user_password(user_id: int, payload: UpdatePasswordRequest, session: Session = Depends(get_session)) -> User:
    return await UserService.update_user_password(user_id, payload, session)


@router.patch('/updateUsername')
async def update_username(user_id: int, payload: UpdateUsernameRequest, session: Session = Depends(get_session)) -> User:
    raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='Service is not available')


@router.patch('/updateEmail')
async def update_user_email(user_id: int, payload: UpdateEmailRequest, session: Session = Depends(get_session)) -> User:
    raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail='Service is not available')
