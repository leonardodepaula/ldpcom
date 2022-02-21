from fastapi import APIRouter

from app.api.endpoints import user, auth, article, log

api_router = APIRouter()
api_router.include_router(user.router, prefix='/user', tags=['users'])
api_router.include_router(auth.router, prefix='/auth', tags=['authentication'])
api_router.include_router(article.router, prefix='/article', tags=['articles'])
api_router.include_router(log.router, prefix='/log', tags=['logs'])