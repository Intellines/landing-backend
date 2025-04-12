import os

import logfire
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request

from contact_us.routers import router as contact_us_router
from logging_config import logger
from schemas import Main

load_dotenv(override=True)

HOST: str | None = os.getenv("HOST")
PORT: str | None = os.getenv("PORT")

if not HOST or not PORT:
    raise ValueError("server Host or Port are not configured")

app: FastAPI = FastAPI(title="Intellines Landing Backend")
app.include_router(contact_us_router)

# bing app to Logfire
logfire.instrument_fastapi(app, capture_headers=True)


@app.get("/", response_model=Main)
async def main(request: Request):
    ip = request.headers.get("x-forwarded-for")
    if ip:
        ip = ip.split(",")[0].strip()
    else:
        ip = request.client.host

    metadata = {"ip": ip}

    return Main(
        **{
            "success": True,
            "service": "Intellines Landing Backend",
            "request_metadata": metadata,
        }
    )


if __name__ == "__main__":
    logger.info(f"starting server at {HOST}:{PORT}")
    uvicorn.run(app=app, host=HOST, port=int(PORT))
