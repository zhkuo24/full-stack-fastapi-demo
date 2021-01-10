# -*- coding: utf-8 -*-
# @File   : __init__.py.py
# @Author : zhkuo
# @Time   : 2021/1/2 6:27 下午
# @Desc   :  

from .crud_user import user
from .crud_item import item


# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
