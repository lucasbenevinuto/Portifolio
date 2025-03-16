from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    owner_id: int


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True 