from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from contact_us.models import ContactUsFormLeads
from contact_us.schemas import ContactUsRequest, ContactUsResponse
from contact_us.services import ContactUsService
from database import get_session
from logging_config import logger

router: APIRouter = APIRouter(prefix='/contact_us', tags=['contact_us'])


@router.get('/all')
async def get_all_contact_us_form_leads(
    session: Session = Depends(get_session),
) -> list[ContactUsFormLeads]:
    leads: list[ContactUsFormLeads] = session.exec(select(ContactUsFormLeads)).all()
    logger.info(f'Found {len(leads)} Contact Us Leads')
    return leads


@router.post('')
async def submit_contact_us(form_data: ContactUsRequest) -> ContactUsResponse:
    return ContactUsService.send_contact_us_to_retool(form_data)
