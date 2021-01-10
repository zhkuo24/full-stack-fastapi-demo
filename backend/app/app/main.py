# -*- coding: utf-8 -*-
# @File   : main.py
# @Author : zhkuo
# @Time   : 2021/1/2 8:44 上午
# @Desc   :  
"""
启动方式： uvicorn main:app --host=127.0.0.1 --port=8080 --reload

采用类似 Flask 的工厂模式来创建APP

"""
from app.api import create_app

app = create_app()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host="127.0.0.1", port=8090, reload=True, debug=True)


