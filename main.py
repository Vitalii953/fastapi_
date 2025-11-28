from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: int 

items = []

@app.get("/")
def home():
    return {"message": "Welcome to the Items API"}

@app.get("/items/")
def read_items():
    return items

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    log.info(f"Item added: {item}. Price: {item.price}")
    return {
    "message": "Item added successfully",
    "item": item, 
    "quantity": len(items)
    }

create_item(Item(name="Sample Item", price=100))