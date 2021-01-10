# -*- coding: utf-8 -*-
# @File   : msg.py
# @Author : zhkuo
# @Time   : 2021/1/10 1:15 上午
# @Desc   : 

from pydantic import BaseModel


class Msg(BaseModel):
    msg: str
