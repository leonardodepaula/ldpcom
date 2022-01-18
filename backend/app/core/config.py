import secrets
from pydantic import AnyHttpUrl, BaseSettings, validator
from typing import List, Union

class Settings(BaseSettings):

    # General FastAPI
    PROJECT_NAME: str
    PROJECT_VERSION: str

    # Database
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    DATABASE_URL: str

    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALLOWED_CORS_ORIGINS: Union[str, List[AnyHttpUrl]]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True
    
    @validator('ALLOWED_CORS_ORIGINS', pre=True)
    def assemble_allowed_cors_origins(cls, value):
        if isinstance(value, str):
            return [item.strip() for item in value.split(',')]
        return value
    
settings = Settings()