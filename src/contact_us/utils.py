import os

import httpx
from dotenv import load_dotenv
from httpx import HTTPStatusError, RequestError, Response

from contact_us.schemas import ContactUsResponse
from logging_config import logger

load_dotenv(override=True)

RETOOL_WORKFLOW_URL = os.getenv("RETOOL_WORKFLOW_URL")
RETOOL_WORKFLOW_API_KEY = os.getenv("RETOOL_WORKFLOW_API_KEY")

if not RETOOL_WORKFLOW_URL or not RETOOL_WORKFLOW_API_KEY:
    raise ValueError("No Workflow API Key or URL")


class ContactUsUtils:
    @staticmethod
    def send_contact_us_to_retool(payload: ContactUsResponse) -> bool | None:
        logger.info(
            f"sending Contact Us form enriched payload to Retool - {payload.model_dump_json()}"
        )

        try:
            response: Response = httpx.post(
                url=RETOOL_WORKFLOW_URL,
                headers={"X-Workflow-Api-Key": RETOOL_WORKFLOW_API_KEY},
                json=payload.model_dump(),
                timeout=10,
            )
            logger.info(
                f"status code - {response.status_code}; response text - {response.text}"
            )
            response.raise_for_status()
        except HTTPStatusError as e:
            logger.error(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
        except RequestError as e:
            logger.error(f"Request error occurred: {e}")
        except Exception as e:
            logger.error(
                f"Unexpected error occurred while sending Contact Us for to Retool - {payload.model_dump_json()}; error - {e}"
            )
        else:
            return True
