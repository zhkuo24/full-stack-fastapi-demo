# -*- coding: utf-8 -*-
# @File   : base.py
# @Author : zhkuo
# @Time   : 2021/1/8 16:08
# @Desc   :

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.base_class import Base

"""
TypeVar，我们可以借助它来自定义兼容特定类型的变量，比如有的变量声明为 int、float、None 都是符合要求的，实际就是代表任意的数字或者空内容
都可以，其他的类型则不可以类型变量还可以用 bound=<type> 指定上限。这里的意思是，（显式或隐式地）取代类型变量的实际类型必须是限定类型的子类
T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, bytes)  # Must be str or bytes

Generic用于泛型类型的抽象基类。泛型类型一般通过继承含一个或多个类型变量的类实例进行声明;

https://cuiqingcai.com/7071.html


Type[C]
一个注解为C的变量可以接受一个类型为C的值。相对地，一个注解为Type[C]的变量可以接受本身为类的值,
更精确地说它接受C的类对象
在一个函数的接收参数中，同时出现"非关键字参数（位置参数）"和"关键字参数"时，可以使用一个单星号来分隔这两种参数
参数*后面均是关键字参数，关键字参数一定要使用"变量名=值"的形式传入数据

jsonable_encoder它接收一个对象，如 Pydantic 模型，并返回JSON兼容版本
"""

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db_session: Session, _id: Any) -> Optional[ModelType]:
        return db_session.query(self.model).filter(self.model.id == _id).first()

    def get_multi(self, db_session: Session, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return db_session.query(self.model).offset(skip).limit(limit).all()

    def create(self, db_session: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    @staticmethod
    def update(db_session: Session, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
               ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            # 将 pydantic 的 BaseModel 类型转为字典
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def remove(self, db_session: Session, *, _id: int) -> ModelType:
        obj = db_session.query(self.model).get(_id)
        db_session.delete(obj)
        db_session.commit()
        return obj


if __name__ == '__main__':
    pass
#     model = BaseModel()
#     test_crud = CRUDBase(model)
#     print(type(model))
#     print(type(test_crud))
