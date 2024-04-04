from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.common.exception.auth import CredentialsException
from app.config.settings import SETTING
from app.crud.user import UserCrud
from app.schemas.token import TokenData

authentication_scheme = HTTPBearer()


async def get_current_user(cred: Annotated[HTTPAuthorizationCredentials, Depends(authentication_scheme)]):
    try:
        token = cred.credentials
        payload = jwt.decode(token, SETTING.SECRET_KEY, algorithms=[SETTING.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise CredentialsException
        token_data = TokenData(email=email)
    except JWTError as e:
        raise CredentialsException from e
    return await UserCrud.get(token_data.email)
