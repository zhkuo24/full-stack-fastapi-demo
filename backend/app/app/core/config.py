# -*- coding: utf-8 -*-
# @File   : config.py
# @Author : zhkuo
# @Time   : 2021/1/2 6:45 下午
# @Desc   :  

"""
reference： https://pydantic-docs.helpmanual.io/usage/settings/
            https://myapollo.com.tw/zh-tw/python-pydantic/
采用 pydantic 中的 BaseSettings 来管理设置
"""

import os
from typing import Optional
from pydantic import BaseSettings
from pydantic import EmailStr, HttpUrl
from dotenv import load_dotenv

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname((os.path.dirname(os.path.abspath(__file__))))), '.env')


# 加载 app下的.env 环境变量
load_dotenv(ENV_PATH)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # 60 minutes * 24 hours * 8days = 8days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # 项目文档信息
    TITLE: str = "FastAPI Demo"
    DESCRIPTION: str = "学习FastAPI的记录"
    DOCS_URL: Optional[str] = None
    OPENAPI_URL: Optional[str] = None
    REDOC_URL: Optional[str] = None
    # SERVER_NAME: str

    PROJECT_NAME: str = "FastAPI Demo"
    SENTRY_DSN: Optional[HttpUrl] = None

    # 数据库路径
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///../test.db"
    # .env中定义的环境变量，BaseSettings可以直接读取到
    TEST: int
    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "test@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin1234"
    USERS_OPEN_REGISTRATION: bool = False
    EMAILS_ENABLED: bool = False

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    class Config:
        env_file = 'ENV_PATH'
        case_sensitive = True


class Production(Settings):
    """
    生产环境
    """
    DEBUG: bool = False


class Development(Settings):
    """
    开发环境
    """
    DEBUG: bool = True

    DOCS_URL = "/api/docs"
    OPENAPI_URL: Optional[str] = "/api/openapi.json"
    REDOC_URL: Optional[str] = "/api/redoc"


def get_settings():
    env = os.getenv('ENV')
    if env == 'PRODUCTION':
        return Production()
    return Development()


settings = get_settings()


if __name__ == '__main__':
    print(settings.DEBUG)


