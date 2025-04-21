import httpx
from fastapi import Request
from httpx import HTTPStatusError, RequestError, Response

from logging_config import logger
from schemas import LocationIP


class Utils:
    @staticmethod
    def get_ip_from_request(request: Request) -> str:
        logger.debug("retrieving IP from the Request")
        x_forwarded_for = request.headers.get("x-forwarded-for")
        if x_forwarded_for:
            logger.debug("IP from proxy headers")
            ip = x_forwarded_for.split(",")[0]
        else:
            logger.debug("IP from client host directly")
            ip = request.client.host

        logger.debug(f"IP - {ip}")
        return ip

    @staticmethod
    def define_location_by_ip(ip: str) -> LocationIP:
        logger.debug(f"get Location by IP - {ip}")

        location: LocationIP = LocationIP(ip=ip, city=None, country=None)
        try:
            response: Response = httpx.get(f"http://ip-api.com/json/{ip}", timeout=10)
            logger.debug(
                f"status code - {response.status_code}; response text - {response.text}"
            )
            response.raise_for_status()

            data = response.json()
            location.city = data.get("city")
            location.country = data.get("country")
            logger.info(
                f"defined location: IP - {ip}; City - {location.city}; Country - {location.country}"
            )

        except HTTPStatusError as e:
            logger.error(
                f"HTTP error occurred: {e.response.status_code} - {e.response.text}"
            )
        except RequestError as e:
            logger.error(f"Request error occurred: {e}")
        except Exception as e:
            logger.error(f"Unexpected error retrieving location for IP {ip}: {e}")

        return location
