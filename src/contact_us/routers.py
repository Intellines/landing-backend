import os
from dotenv import load_dotenv

from utils import Utils
from schemas import LocationIP

from logging_config import logger
from fastapi import APIRouter, Request
from contact_us.schemas import ContactUsRequest, ContactUsResponse

load_dotenv(override=True)

RETOOL_WORKFLOW_URL = os.getenv("RETOOL_WORKFLOW_URL")
RETOOL_WORKFLOW_API_KEY = os.getenv("RETOOL_WORKFLOW_API_KEY")

if not RETOOL_WORKFLOW_URL or not RETOOL_WORKFLOW_API_KEY:
    raise ValueError("No Workflow API Key or URL")


router: APIRouter = APIRouter(prefix="/contact_us", tags=["contact_us"])


@router.post("/", response_model=ContactUsResponse)
async def submit_contact_us(form_data: ContactUsRequest, request: Request):
    logger.info(f"Contact Us form submitted - {form_data.model_dump_json()}")

    ip: str = Utils.get_ip_from_request(request)
    logger.info(f"IP - {ip}")

    location: LocationIP = Utils.define_location_by_ip(ip)
    logger.info(f"Location by IP - {location}")


    return ContactUsResponse(**form_data.model_dump(), ip=ip, city=location.city, country=location.country)
