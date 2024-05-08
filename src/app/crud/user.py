import uuid

from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from app.common.auth.authenticator import Authenticator
from app.common.exception.user import (
    UserExistsError,
    EmailValidationError,
    PasswordValidationError,
)
from app.models import User
from app.schemas.user import UserSignUp


class UserCrud:
    @classmethod
    async def create(cls, user: UserSignUp) -> User:
        cls.validate_email(user.email)
        cls.validate_password(user.password)
        # Check user exists
        if await User.objects.filter(email=user.email).aexists():
            raise UserExistsError(e="Email already exists")
        # Create user
        user.password = Authenticator.get_hashed_password(user.password)
        return await User.objects.acreate(
            email=user.email, password=user.password, username=user.username, full_name=user.full_name
        )

    @classmethod
    async def get(cls, email: str) -> User:
        return await User.objects.filter(email=email).afirst()

    @classmethod
    def get_scoreboard(cls, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size
        return list(User.objects.order_by("-score").all()[offset : offset + page_size])

    @classmethod
    async def get_by_uuid(cls, user_id: uuid.UUID) -> User:
        return await User.objects.filter(uuid=user_id).afirst()

    @staticmethod
    def validate_email(email: str) -> None:
        try:
            validate_email(email)
        except Exception as e:
            raise EmailValidationError(e=e.messages) from e

    @staticmethod
    def validate_password(password: str) -> None:
        try:
            validate_password(password)
        except Exception as e:
            raise PasswordValidationError(e=list(e.messages)) from e
