from fastapi import APIRouter

from contact_us.schemas import ContactUsRequest, ContactUsResponse
from contact_us.services import ContactUsService

router: APIRouter = APIRouter(prefix="/contact_us", tags=["contact_us"])


@router.post("/", response_model=ContactUsResponse)
async def submit_contact_us(form_data: ContactUsRequest):
    return ContactUsService.send_contact_us_to_retool(form_data)
