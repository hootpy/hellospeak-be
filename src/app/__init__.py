from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    from app.apis.routes import router as api_router

    app = FastAPI(
        title="HelloSpeak BE",
        version="0.1.0",
        description="Backend for HelloSpeak",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")

    return app
