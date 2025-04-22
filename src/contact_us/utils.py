import httpx
from httpx import HTTPStatusError, Response

from config import config
from contact_us.schemas import ContactUsResponse
from logging_config import logger


class ContactUsUtils:
    @staticmethod
    def send_contact_us_to_retool(payload: ContactUsResponse) -> None:
        logger.debug(f'Sending - {payload.model_dump_json()}')
        try:
            response: Response = httpx.post(
                url=config.RETOOL_WORKFLOW_URL,
                headers={'X-Workflow-Api-Key': config.RETOOL_WORKFLOW_API_KEY},
                json=payload.model_dump(),
                timeout=10,
            )
            logger.info(
                f'Retool response: status code - {response.status_code}; response text - {response.text}'
            )
            response.raise_for_status()
        except HTTPStatusError as e:
            logger.error(
                f'Error occurred while sending Contact Us form to Retool - {payload.model_dump_json()}; error - {e}'
            )
