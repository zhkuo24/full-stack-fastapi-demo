# -*- coding: utf-8 -*-
# @File   : user.py
# @Author : zhkuo
# @Time   : 2021/1/2 11:32 下午
# @Desc   : 

from typing import Optional

from pydantic import BaseModel, EmailStr


# Base Model
class UserBase(BaseModel):
    email: Optional[str] = None
    is_activate: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = None


# 定义兼容 ORM
class UserBaseInDB(UserBase):
    id: int = None

    class Config:
        orm_mode = True


# 定义与 API 接口相关的数据类型
# 新建用户，接收 email 和 password
# EmailStr 相当于一个验证器  email-validator 满足 email的格式
class UserCreate(UserBase):
    email: EmailStr
    password: str


# 更新用户
class UserUpdate(UserBaseInDB):
    password: Optional[str] = None


# API 返回的 User 模型
class User(UserBaseInDB):
    pass


# 存储在数据库中的 User 模型
# 密码不能保持明文
class UserInDB(UserBaseInDB):
    hashed_password: str
