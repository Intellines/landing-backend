from pydantic import BaseModel


class GetTokenRequest(BaseModel):
    email: str
    password: str
