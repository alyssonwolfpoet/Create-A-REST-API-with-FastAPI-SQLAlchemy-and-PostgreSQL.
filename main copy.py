from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel): #serialize
    id:int
    name:str
    description:str
    price:int
    on_offer:bool

@app.get("/")
def index():
    return {"Messege":"Hello World"}

@app.get("/greet/{name}")
def greet_name(name:str):
    return {"greeting":f"Hello {name}"}

@app.get("/greet")
def greet_opcional_name(name:Optional[str]="user"):
    return {"Messege": f"Hello {name}"}

@app.put("/item/{item_id}")
def update_item(item_id:int,item:Item):
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "on_offer": item.on_offer
    }