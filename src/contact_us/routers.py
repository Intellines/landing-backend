from fastapi import APIRouter, HTTPException, Request, status

from contact_us.schemas import ContactUsRequest, ContactUsResponse
from contact_us.utils import ContactUsUtils
from logging_config import logger
from schemas import LocationIP
from utils import Utils

router: APIRouter = APIRouter(prefix="/contact_us", tags=["contact_us"])


@router.post("/", response_model=ContactUsResponse)
async def submit_contact_us(form_data: ContactUsRequest, request: Request):
    logger.info(f"Contact Us form submitted - {form_data.model_dump_json()}")

    ip: str = Utils.get_ip_from_request(request)
    logger.info(f"IP - {ip}")

    location: LocationIP = Utils.define_location_by_ip(ip)
    logger.info(f"Location by IP - {location}")

    payload: ContactUsResponse = ContactUsResponse(
        **form_data.model_dump(), ip=ip, city=location.city, country=location.country
    )

    sent_to_retool: bool | None = ContactUsUtils.send_contact_us_to_retool(payload)
    if sent_to_retool is not True:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Contact Us Form processing failed on the Retool side",
        )

    return payload
