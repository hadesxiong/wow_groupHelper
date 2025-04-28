# coding=utf8

from typing import List, Union

from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    WECHAT_TOKEN: str
    WECHAT_AESKEY: str
    WECHAT_APPID: str
    WECHAT_APPSECRET: str

    DB_HOST: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_SCHEMA: str

    SECRET_KEY: str
    ALGORITHM: str

    @field_validator("BACKEND_CORS_ORIGINS", check_fields="before")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
