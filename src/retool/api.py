from httpx import Response, AsyncClient
from config import config
from retool.schemas import RetoolEmailPayload
from logging_config import logger


class RetoolAPI:
    RETOOL_EMAIL_URL = config.RETOOL_EMAIL_URL
    RETOOL_EMAIL_API_KEY = config.RETOOL_EMAIL_API_KEY

    @classmethod
    async def send_email_via_retool(cls, email_payload: RetoolEmailPayload) -> None:
        logger.info(f'Sending Email via Retool - {email_payload.model_dump_json(indent=2)}')
        client: AsyncClient = AsyncClient()
        try:
            response: Response = await client.post(
                url=cls.RETOOL_EMAIL_URL,
                headers={'X-Workflow-Api-Key': cls.RETOOL_EMAIL_API_KEY},
                json=email_payload.model_dump(),
                timeout=30,
            )
            logger.debug(response.status_code)
            logger.debug(response.text)
            response.raise_for_status()
        except Exception:
            logger.error('API Error on /send_email_via_retool')
