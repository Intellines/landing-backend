from all_schemas import LocationIP
from all_utils import Utils
from contact_us.schemas import ContactUsRequest, ContactUsResponse
from contact_us.utils import ContactUsUtils
from logging_config import logger


class ContactUsService:
    @staticmethod
    def send_contact_us_to_retool(form_data: ContactUsRequest) -> ContactUsResponse:
        logger.info(f'Contact Us form submitted - {form_data.model_dump_json()}')
        contact_us_response: ContactUsResponse = ContactUsResponse(
            **form_data.model_dump()
        )
        if ip := form_data.ip:
            location: LocationIP = Utils.define_location_by_ip(ip)
            contact_us_response.city = location.city
            contact_us_response.country = location.country

        ContactUsUtils.send_contact_us_to_retool(contact_us_response)
        return contact_us_response
