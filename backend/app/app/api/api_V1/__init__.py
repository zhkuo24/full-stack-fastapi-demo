# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : zhkuo
# @Time   : 2021/1/2 6:26 下午
# @Desc   :

"""
路由区分
"""

from fastapi import APIRouter
from app.api.api_V1.endpoints import items, users, login


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix='/users', tags=['users'])
api_router.include_router(items.router, prefix='/items', tags=['items'])

