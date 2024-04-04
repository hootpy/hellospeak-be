from datetime import timedelta, datetime, timezone

from jose import jwt
from passlib.context import CryptContext

from app.config.settings import SETTING


class Authenticator:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_hashed_password(cls, password):
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def create_access_token(cls, data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode |= {"exp": expire}
        return jwt.encode(to_encode, SETTING.SECRET_KEY, algorithm=SETTING.ALGORITHM)
