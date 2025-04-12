from fastapi import Request
from logging_config import logger
from schemas import LocationIP
import httpx
from httpx import Response

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
            response: Response = httpx.get(f"http://ip-api.com/json/24.48.0.1{ip}", timeout=10)
            logger.debug(f"status code - {response.status_code}; response text - {response.text}")
            response.raise_for_status()
            
            data = response.json()
            location.city = data.get("city")
            location.country = data.get("country")
            logger.debug(f"defined location: IP - {ip}; City - {location.city}; Country - {location.country}")

        except Exception as ex:
            logger.error(f"unable to define Location by IP - {ip}; error - {ex}")

        finally:
            return location


            
            
        