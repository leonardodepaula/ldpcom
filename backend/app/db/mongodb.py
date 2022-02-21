from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

mongodb_client = AsyncIOMotorClient(settings.MONGODB_URI)