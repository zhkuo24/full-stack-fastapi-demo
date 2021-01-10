# -*- coding: utf-8 -*-
# @File   : tmp_main.py
# @Author : zhkuo
# @Time   : 2021/1/3 8:40 上午
# @Desc   : 

from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


if __name__ == '__main__':
    import uvicorn
    # uvicorn.run(app='tmp_main:app', host="127.0.0.1", port=8090, reload=True, debug=True)
    from pydantic import BaseModel
    from fastapi.encoders import jsonable_encoder
    from fastapi import Depends


    # Item 的基类
    class ItemBase(BaseModel):
        title: str = None
        dsecription: str = None

    item = ItemBase()
    item.title = "sss"
    item.dsecription = "sasas"

    # print(type(jsonable_encoder(item)))
    # print(jsonable_encoder(item))

    def gen():
        try:
            a = "sssssaa"
            print('try')
            yield a
        finally:
            print("I am done")

    # for i in gen():
    #     print(i)
    a = Depends(gen)
    print("ss", type(a))


    async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
        return {"q": q, "skip": skip, "limit": limit}


    commons: dict = Depends(common_parameters)
    print(commons)