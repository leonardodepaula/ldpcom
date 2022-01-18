from fastapi import APIRouter

from app.api.endpoints import user, auth

api_router = APIRouter()
api_router.include_router(user.router, prefix='/user', tags=['users'])
api_router.include_router(auth.router, prefix='/auth', tags=['authentication'])