from datetime import timedelta

from fastapi import APIRouter

from app.common.auth.authenticator import Authenticator
from app.common.auth.user import UserAuthenticator
from app.config.settings import SETTING
from app.crud.user import UserCrud
from app.schemas.token import Token
from app.schemas.user import UserSignUp, UserSignUpResponse, UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/signup")
async def signup(user: UserSignUp) -> UserSignUpResponse:
    """
    Sign up a new user.
    """
    user = await UserCrud.create(user)
    return UserSignUpResponse.model_validate(user)


@router.post("/login")
async def login(user: UserLogin) -> Token:
    """
    Use login
    """
    user = await UserAuthenticator.authenticate_user(user)

    access_token_expires = timedelta(minutes=SETTING.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = Authenticator.create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")
