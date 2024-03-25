from fastapi import FastAPI


def create_app() -> FastAPI:
    from app.apis.routes import router as api_router

    app = FastAPI(
        title="HelloSpeak BE",
        version="0.1.0",
        description="Backend for HelloSpeak",
    )

    app.include_router(api_router, prefix="/api")

    return app
