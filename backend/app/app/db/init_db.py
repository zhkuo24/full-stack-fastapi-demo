# -*- coding: utf-8 -*-
# @File   : init_db.py
# @Author : zhkuo
# @Time   : 2021/1/9 1:11 下午
# @Desc   : 

from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db_session: Session):
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud.user.get_by_email(db_session, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True
        )
        user = crud.user.create(db_session, obj_in=user_in)

