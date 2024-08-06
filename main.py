from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app = FastAPI()

class Item(BaseModel): #serialize
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

    class Config:
        orm_mode = True

db=SessionLocal()

@app.get("/items",response_model=List[Item],status_code=200)
def get_all_items():
    items = db.query(models.Item).all()
    return items

@app.get("/items/{item_id}")
def get_an_item(item_id:int):
    pass

@app.post("/items")
def create_an_item():
    pass

@app.put("/item/{item_id}")
def update_an_item(item_id:int):
    pass

@app.delete("item/{item_id}")
def delete_item(item_id:int):
    pass