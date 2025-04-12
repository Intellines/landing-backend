from contact_us.schemas import ContactUsRequest, ContactUsResponse
from contact_us.utils import ContactUsUtils
from logging_config import logger
from schemas import LocationIP
from utils import Utils


class ContactUsService:
    @staticmethod
    def send_contact_us_to_retool(form_data: ContactUsRequest) -> ContactUsResponse:
        logger.info(f"Contact Us form submitted - {form_data.model_dump_json()}")

        ip: str = form_data.ip
        logger.info(f"Client IP - {ip}")

        location: LocationIP = Utils.define_location_by_ip(ip)
        logger.info(f"Location by IP - {location}")

        contact_us_response: ContactUsResponse = ContactUsResponse(
            **form_data.model_dump(), city=location.city, country=location.country
        )

        # send form payload to Retool to send Email and save form data to DB
        ContactUsUtils.send_contact_us_to_retool(contact_us_response)

        return contact_us_response
