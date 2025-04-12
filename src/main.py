import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request

from schemas import Main

load_dotenv(override=True)

HOST = os.getenv("HOST", None)
PORT = os.getenv("PORT", 0)

if not HOST or not PORT:
    raise ValueError("server Host or Port are not configured")

app = FastAPI(title="Intellines Landing Backend")


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
    uvicorn.run(app=app, host=HOST, port=int(PORT))
