from passlib.context import CryptContext


class UserUtils:
    pwd_context: CryptContext = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def generate_password_hash(cls, password: str) -> str:
        return cls.pwd_context.hash(password)

    @classmethod
    def validate_password(cls, password: str, password_hash: str) -> bool:
        return cls.pwd_context.verify(password, password_hash)
