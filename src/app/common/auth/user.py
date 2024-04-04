from app.common.auth.authenticator import Authenticator
from app.common.exception.user import UserNotFoundError, PasswordIncorrectError
from app.crud.user import UserCrud
from app.schemas.user import UserLogin


class UserAuthenticator:
    @classmethod
    async def authenticate_user(cls, user_schema: UserLogin) -> UserLogin:
        user = await UserCrud.get(user_schema.email)
        if not user:
            raise UserNotFoundError(e="User not found")
        if not Authenticator.verify_password(user_schema.password, user.password):
            raise PasswordIncorrectError(e="Password is incorrect")
        return user_schema
