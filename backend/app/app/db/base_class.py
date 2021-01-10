# -*- coding: utf-8 -*-
# @File   : base_class.py
# @Author : zhkuo
# @Time   : 2021/1/3 9:58 上午
# @Desc   : model基础模块 如通用字段

from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """通用字段"""
    id: Any
    __name__: str

    # 自动生成表名
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

