from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DATABASE: str
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str

    ALLOW_ORIGINS: list[str] = ["*"]
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list[str] = ["*"]
    ALLOW_HEADERS: list[str] = ["*"]

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        case_sensitive = True
        env_file = ".env"


SETTING = Setting()
