"""Simple FastAPI application with GET and POST endpoints."""
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI!"}


@app.post("/items")
async def create_item(name: str = Body(..., embed=True)) -> dict[str, str]:
    return {"message": f"Item received: {name}"}
