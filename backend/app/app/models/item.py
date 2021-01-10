# -*- coding: utf-8 -*-
# @File   : item.py
# @Author : zhkuo
# @Time   : 2021/1/3 9:21 上午
# @Desc   : 

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
