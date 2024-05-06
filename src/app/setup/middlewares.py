from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware


middlewares = [
    Middleware(
        CORSMiddleware,
    )
]
