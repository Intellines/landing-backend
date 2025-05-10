from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from contact_us.models import ContactUsFormLead
from contact_us.schemas import ContactUsRequest, ContactUsResponse
from contact_us.services import ContactUsService
from database import get_session
from logging_config import logger

router: APIRouter = APIRouter(prefix='/contact_us', tags=['contact_us'])


@router.get('/all')
async def get_all_contact_us_form_leads(
    session: Session = Depends(get_session),
) -> list[ContactUsFormLead]:
    leads: list[ContactUsFormLead] = session.exec(select(ContactUsFormLead)).all()
    logger.info(f'Found {len(leads)} Contact Us Leads')
    return leads


@router.post('')
async def submit_contact_us(form_data: ContactUsRequest, session: Session = Depends(get_session)) -> ContactUsFormLead:
    return await ContactUsService.submit_contact_us_form(form_data, session)
