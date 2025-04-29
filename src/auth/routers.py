from fastapi import APIRouter, Depends
from sqlmodel import Session

from all_models import User
from auth.schemas import TokenRequest, Token
from auth.services import AuthService
from database import get_session

from auth.dependencies import AuthDependencies

router: APIRouter = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token')
async def get_auth_token(payload: TokenRequest, session: Session = Depends(get_session)) -> Token:
    return await AuthService.authenticate_user(payload.email, payload.password, session)


@router.post('/decodeToken')
async def decode_token(token: str) -> dict | None:
    return await AuthService.decode_token(token)


@router.get('/test')
async def test_auth(current_user: User = Depends(AuthDependencies.get_current_user)) -> dict:
    return {'email': current_user.email, 'username': current_user.username}
