from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    token: str
    token_type: str

