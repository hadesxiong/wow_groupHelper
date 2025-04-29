# coding=utf8

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings
from app.core.error import add_exception_handlers
from app.api.routers import *

import app.core.db as db_base

def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app

app = get_application()

app.include_router(base_rt)
app.include_router(group_rt)

register_tortoise(
    app,
    config = db_base.tortoise_cfg,
    modules = db_base.modules,
    generate_schemas = True,
    add_exception_handlers = True
)

add_exception_handlers(app)
add_pagination(app)