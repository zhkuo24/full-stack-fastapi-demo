# -*- coding: utf-8 -*-
# @File   : items.py
# @Author : zhkuo
# @Time   : 2021/1/3 8:57 上午
# @Desc   : 

from pydantic import BaseModel

from .user import User


# Item 的基类
class ItemBase(BaseModel):
    title: str = None
    dsecription: str = None


# 生成 Item 的模型, title 为必需的值
class ItemCreate(ItemBase):
    title: str


# 更新 Item
class ItemUpdate(ItemBase):
    pass


# 存储在数据库中的 Item 模型，基类
class ItemInDBBase(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# API 返回给客户端的模型
class Item(ItemBase):
    pass


# 存储在数据库中的 Item 模型
class ItemInDB(ItemInDBBase):
    pass

