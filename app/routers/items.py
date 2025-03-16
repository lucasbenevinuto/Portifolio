from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter()

# Simulação de banco de dados
items_db = []

@router.get("/", response_model=List[Item])
async def read_items():
    return items_db

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    new_item = Item(id=len(items_db) + 1, **item.dict())
    items_db.append(new_item)
    return new_item

@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    for i, stored_item in enumerate(items_db):
        if stored_item.id == item_id:
            update_data = item.dict(exclude_unset=True)
            updated_item = stored_item.copy(update=update_data)
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found") 