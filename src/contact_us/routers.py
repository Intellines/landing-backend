import os
from dotenv import load_dotenv

from logging_config import logger
from fastapi import APIRouter, Request
from contact_us.schemas import ContactUsRequest, ContactUsResponse

load_dotenv(override=True)

RETOOL_WORKFLOW_URL = os.getenv("RETOOL_WORKFLOW_URL")
RETOOL_WORKFLOW_API_KEY = os.getenv("RETOOL_WORKFLOW_API_KEY")

if not RETOOL_WORKFLOW_URL or not RETOOL_WORKFLOW_API_KEY:
    raise ValueError("No Workflow API Key or URL")


router: APIRouter = APIRouter(prefix="/contact_us", tags=["contact_us"])


@router.port("/", response_model=ContactUsResponse)
async def submit_contact_us(form_data: ContactUsRequest):
    logger.info(f"Contact Us form submitted - {form_data.model_dump_json()}")
    response: ContactUsResponse = ContactUsResponse()

    for key, value in form_data.model_dump().items():
        setattr(response, key, value)
    
    ip: str = "test"
    response.ip = ip
    return response

