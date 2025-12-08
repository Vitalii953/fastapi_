import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

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

    id: int | None = None
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, description="Price must be greater than zero")


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
    return {"message": "Item added successfully", "added": item, "quantity": len(items)}
