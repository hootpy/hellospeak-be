from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

from app.config.settings import SETTING

middlewares = [
    Middleware(
        CORSMiddleware,
        allow_origins=SETTING.ALLOW_ORIGINS,
        allow_credentials=SETTING.ALLOW_CREDENTIALS,
        allow_methods=SETTING.ALLOW_METHODS,
        allow_headers=SETTING.ALLOW_HEADERS,
    )
]
