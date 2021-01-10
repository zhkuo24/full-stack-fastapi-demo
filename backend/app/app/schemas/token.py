# -*- coding: utf-8 -*-
# @File   : token.py
# @Author : zhkuo
# @Time   : 2021/1/9 10:22 下午
# @Desc   : 


from typing import Optional

from pydantic import BaseModel

"""
jwt认证 https://www.ruanyifeng.com/blog/2018/07/json_web_token-tutorial.html
"""


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
