from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import Any

from all_models import User
from auth.schemas import TokenRequest, Token
from auth.services import AuthService
from database import get_session

router: APIRouter = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token')
async def get_auth_token(payload: TokenRequest, session: Session = Depends(get_session)) -> Token:
    return await AuthService.authenticate_user(payload.email, payload.password, session)


@router.post('/decodeToken')
async def decode_token(token: str) -> dict | None:
    return await AuthService.decode_token(token)
