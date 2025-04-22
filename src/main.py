from typing import Annotated

import logfire
import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from config import config
from contact_us.routers import router as contact_us_router
from logging_config import logger
from schemas import MainResponse
from utils import Utils

app: FastAPI = FastAPI(title='Intellines Landing Backend')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(contact_us_router)

logfire.instrument_fastapi(app, capture_headers=True)


@app.get('/')
async def main(
    request: Request, token: Annotated[str, Depends(oauth2_scheme)]
) -> MainResponse:
    return MainResponse(
        **{
            'success': True,
            'service': 'Intellines Landing Backend',
            'ip': Utils.get_ip_from_request(request=request),
        }
    )


if __name__ == '__main__':
    logger.info(f'starting server at {config.HOST}:{config.PORT}')
    uvicorn.run(app=app, host=config.HOST, port=config.PORT)
