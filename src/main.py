import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    """Data model for an item."""

    name: str
    price: int


items = []


@app.get("/")
def home():
    """Home endpoint returning a welcome message."""
    return {"message": "Welcome to the Items API"}


@app.get("/items/")
def read_items():
    """Retrieve the list of items."""
    return items


@app.post("/items/")
def create_item(item: Item):
    """Create a new item and add it to the list."""
    items.append(item)
    log.info("Item added: %s. Price: %s", item.name, item.price)
    return {"message": "Item added successfully", "item": item, "quantity": len(items)}


create_item(Item(name="Sample Item", price=100))
