from sqlmodel import Session

from logging_config import logger
from all_schemas import LocationIP
from all_utils import Utils
from all_models import ContactUsFormLead

from contact_us.schemas import ContactUsRequest, ContactUsResponse, ContactUsLeadCreate
from contact_us.utils import ContactUsUtils


class ContactUsService:
    @staticmethod
    async def submit_contact_us_form(form_data: ContactUsRequest, session: Session) -> ContactUsFormLead:
        logger.info(f'Contact Us form submitted - {form_data.model_dump_json()}')
        contact_us_response: ContactUsResponse = ContactUsResponse(**form_data.model_dump())
        if ip := form_data.ip:
            location: LocationIP = Utils.define_location_by_ip(ip)
            contact_us_response.city = location.city
            contact_us_response.country = location.country

        contact_us: ContactUsLeadCreate = ContactUsLeadCreate(**contact_us_response.model_dump())
        contact_us_db: ContactUsFormLead = ContactUsFormLead(**contact_us.model_dump())
        session.add(contact_us_db)
        session.commit()
        session.refresh(contact_us_db)
        return contact_us_db
