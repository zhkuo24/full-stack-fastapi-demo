# -*- coding: utf-8 -*-
# @File   : session.py
# @Author : zhkuo
# @Time   : 2021/1/3 9:12 下午
# @Desc   : 

from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

"""
参考:
https://www.osgeo.cn/sqlalchemy/orm/session_basics.html
https://landybird.github.io/python/2020/03/02/fastapi%E4%B8%8Easgi(5)/
处理session的不同方法 https://github.com/tiangolo/fastapi/issues/726
处理数据库session的方法
1. sqlalchemy.orm 自带的 scoped_session
2. 采用中间件的方法，每个请求建立一个 db 连接 
3. dependency 依赖的方法(官方文档推荐方法）
"""

# 创建连接数据库的 engine
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
# 为了保证线程安全，需使用scoped_session方法
# db_session = scoped_session(
#     sessionmaker(autocommit=False, autoflush=False, bind=engine)
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
