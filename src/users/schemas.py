from pydantic import BaseModel, EmailStr, constr

PasswordStr: constr = constr(min_length=8, max_length=50)
UsernameStr: constr = constr(min_length=8, max_length=16)


class UserCreate(BaseModel):
    username: UsernameStr
    email: EmailStr
    password: PasswordStr


class UpdatePasswordRequest(BaseModel):
    user_id: int
    old_password: str
    new_password: PasswordStr


class UpdateUsernameRequest(BaseModel):
    user_id: int
    old_username: str
    new_username: UsernameStr


class UpdateEmailRequest(BaseModel):
    user_id: int
    old_email: str
    new_email: EmailStr
