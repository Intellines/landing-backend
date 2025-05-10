from fastapi import APIRouter
from retool.schemas import RetoolEmailPayload
from retool.api import RetoolAPI


router: APIRouter = APIRouter(prefix='/retool', tags=['retool'])


@router.post(path='/send_email')
async def send_email_via_retool(email_payload: RetoolEmailPayload) -> RetoolEmailPayload:
    await RetoolAPI.send_email_via_retool(email_payload)
    return email_payload
