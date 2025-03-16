from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: str = None
    email: str = None
    password: str = None
    is_active: bool = None


class User(UserBase):
    id: int

    class Config:
        from_attributes = True 