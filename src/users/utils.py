from passlib.context import CryptContext


class UserUtils:
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @staticmethod
    def generate_password_hash(password: str) -> str:
        return UserUtils.pwd_context.hash(password)

    @staticmethod
    def validate_password(password: str, password_hash: str) -> bool:
        return UserUtils.pwd_context.verify(password, password_hash)


if __name__ == '__main__':
    test_pass: str = '12345678'
    hash: str = UserUtils.generate_password_hash(test_pass)
    print(hash)

    valid_pass: bool = UserUtils.validate_password('12345679', hash)
    print(valid_pass)