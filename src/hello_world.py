from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}/")
def read_item(item_id: int, query: Optional[str] = None, query2: Optional[str] = None):
    response = {"item_id": item_id, "query": query}
    if query:
        response["query"] = query
    if query2:
        response["query2"] = query2
    return response


class Item(BaseModel):
    name: str


@app.post("/items/")
def create_item(name: Item):
    return {"name": name.name, "status": "cachorro feliz (OK)"}
