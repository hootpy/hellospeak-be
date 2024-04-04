from fastapi import HTTPException
from starlette import status


class EmailValidationError(HTTPException):
    def __init__(self, e: list[str]):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


class PasswordValidationError(HTTPException):
    def __init__(self, e: list[str]):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


class UserExistsError(HTTPException):
    def __init__(self, e: str):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


class UserNotFoundError(HTTPException):
    def __init__(self, e: list[str]):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e,
            headers={"WWW-Authenticate": "Bearer"},
        )


class PasswordIncorrectError(HTTPException):
    def __init__(self, e: list[str]):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=e)
