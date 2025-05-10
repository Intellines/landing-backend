import asyncio
from sqlmodel import Session

from logging_config import logger
from config import config
from all_schemas import LocationIP
from all_utils import Utils
from all_models import ContactUsFormLead

from contact_us.schemas import ContactUsRequest, ContactUsResponse

# from contact_us.utils import ContactUsUtils
from retool.api import RetoolAPI
from retool.schemas import RetoolEmailPayload
from contact_us.email_templates import contact_us_email


class ContactUsService:
    @staticmethod
    async def _add_location_to_payload(response: ContactUsResponse, form_data: ContactUsRequest):
        if ip := form_data.ip:
            location: LocationIP = Utils.define_location_by_ip(ip)
            response.city = location.city
            response.country = location.country

    @classmethod
    async def submit_contact_us_form(cls, form_data: ContactUsRequest, session: Session) -> ContactUsFormLead:
        logger.info(f'Contact Us form submitted - {form_data.model_dump_json()}')
        contact_us_response: ContactUsResponse = ContactUsResponse(**form_data.model_dump())

        # send email to the team
        asyncio.create_task(
            RetoolAPI.send_email_via_retool(
                email_payload=RetoolEmailPayload(
                    emails=[config.ADMIN_EMAIL],
                    subject='📮 Contact Us Form submitted',
                    body=contact_us_response.model_dump_json(indent=2),
                )
            )
        )

        # send contact us email to the lead
        await RetoolAPI.send_email_via_retool(
            email_payload=RetoolEmailPayload(
                emails=[contact_us_response.email], subject='🤝 Thank you for Reaching Out!', body=contact_us_email
            )
        )

        # enrich ip with location
        await cls._add_location_to_payload(response=contact_us_response, form_data=form_data)
        contact_us_db: ContactUsFormLead = ContactUsFormLead(**contact_us_response.model_dump())

        # save lead to db
        session.add(contact_us_db)
        session.commit()
        session.refresh(contact_us_db)

        return contact_us_db
