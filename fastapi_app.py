from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data Model (Schema)
class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: Optional[bool] = None

# In-memory database
db = []

# CREATE: Add a new item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    db.append(item)
    return item

# READ: Get all items or a specific one
@app.get("/items/", response_model=List[Item])
def read_items():
    return db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# UPDATE: Modify an existing item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(db):
        if item.id == item_id:
            db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE: Remove an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item.id == item_id:
            db.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
