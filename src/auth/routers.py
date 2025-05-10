from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from user.models import User
from auth.dependencies import AuthDependencies
from auth.schemas import Token, TokenRequest
from auth.services import AuthService
from database import get_session
from logging_config import logger

router: APIRouter = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token')
async def get_auth_token(payload: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)) -> Token:
    return await AuthService.authenticate_user(payload.username, payload.password, session)


@router.post('/decodeToken')
async def decode_token(token: str) -> dict | None:
    return await AuthService.decode_token(token)


@router.get('/profile')
async def get_profile(current_user: User = Depends(AuthDependencies.get_current_user)) -> User:
    return current_user
