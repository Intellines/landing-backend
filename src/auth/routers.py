from fastapi import APIRouter, Depends
from sqlmodel import Session

from all_models import User
from auth.schemas import GetTokenRequest
from auth.services import AuthService
from database import get_session

router: APIRouter = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token')
async def get_auth_token(payload: GetTokenRequest, session: Session = Depends(get_session)) -> User:
    return await AuthService.authenticate_user(payload.email, payload.password, session)
