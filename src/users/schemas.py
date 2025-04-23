from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    username: constr(min_length=8, max_length=16)
    email: EmailStr
    password: constr(min_length=8, max_length=50)
