from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.config.settings import SETTING


def create_app() -> FastAPI:
    from app.apis.routes import router as api_router

    app = FastAPI(
        title="HelloSpeak BE",
        version="0.1.0",
        description="Backend for HelloSpeak",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=SETTING.ALLOW_ORIGINS,
        allow_credentials=SETTING.ALLOW_CREDENTIALS,
        allow_methods=SETTING.ALLOW_METHODS,
        allow_headers=SETTING.ALLOW_HEADERS,
    )
    app.include_router(api_router, prefix="/api")

    return app
