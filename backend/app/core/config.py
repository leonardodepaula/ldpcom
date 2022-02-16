import secrets
import pathlib

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator, DirectoryPath
from typing import Any, Dict, List, Optional, Union

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
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    # Security
    SECRET_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: Union[str, List[AnyHttpUrl]] = []
    ENCRYPTION_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # Directories
    BASE_DIR: Optional[DirectoryPath] = None
    STATIC_DIR: Optional[DirectoryPath] = None

    @validator("BASE_DIR")
    def get_base_dir(cls, v: str):
        return pathlib.Path(__file__).parent.resolve().parent.absolute()
    
    @validator("STATIC_DIR")
    def get_static_dir(cls, value, values):
        return pathlib.Path(values['BASE_DIR'])/'static'

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme='postgresql',
            user=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_SERVER'),
            port=values.get('POSTGRES_PORT'),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True
    
settings = Settings()