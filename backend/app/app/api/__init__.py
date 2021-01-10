# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : zhkuo
# @Time   : 2021/1/2 6:26 下午
# @Desc   :  

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.api_V1 import api_router


def register_cors(app: FastAPI) -> None:
    """
    支持跨域
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_router(app: FastAPI) -> None:
    """
    注册路由
    """
    app.include_router(
        api_router,
        prefix=settings.API_V1_STR
    )


def create_app() -> FastAPI:
    """
    生产 FastAPI的对象
    :return:
    """
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        openapi_url=settings.OPENAPI_URL,
        redoc_url=settings.REDOC_URL
    )

    # 其他相关设置，中间件等
    # 跨域设置
    register_cors(app)
    # 注册路由
    register_router(app)
    return app

