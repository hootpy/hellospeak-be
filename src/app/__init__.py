from fastapi import FastAPI

from app.setup import middlewares


def create_app() -> FastAPI:
    from app.apis.routes import router as api_router

    app = FastAPI(
        title="HelloSpeak BE",
        version="0.1.0",
        description="Backend for HelloSpeak",
        middleware=middlewares,
    )

    app.include_router(api_router, prefix="/api")

    return app
