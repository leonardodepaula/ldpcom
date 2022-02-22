from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.api.base import api_router
from app.core.middleware import RequestLogMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(api_router)

app.add_middleware(
  CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.add_middleware(RequestLogMiddleware)

app.mount('/static', StaticFiles(directory='app/static'), name='static')