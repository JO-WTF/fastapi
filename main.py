"""Simple FastAPI application with GET and POST endpoints."""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    """Return a simple greeting message."""
    return {"message": "Hello from FastAPI!"}


class Item(BaseModel):
    """Request body model for the POST endpoint."""

    name: str
    description: Optional[str] = None


@app.post("/items")
async def create_item(item: Item) -> dict:
    """Echo the received item data back to the client."""
    return {"message": "Item received", "item": item}
