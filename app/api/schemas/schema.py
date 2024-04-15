from typing import Optional

from pydantic import BaseModel


class SQLCondition(BaseModel):
    def where(self):
        where = {}
        for field in self.model_fields.keys():
            value = getattr(self, field)
            if any([not value, field.startswith("new_"), field in ["limit", "offset"]]):
                continue
            where[field] = value
        return where

    def values(self):
        values = {}
        for field in self.model_fields.keys():
            value = getattr(self, field)
            if any(
                [
                    value is None,
                    not field.startswith("new_"),
                    field in ["limit", "offset"],
                ]
            ):
                continue
            # print(f"{field=}")
            values[field.split("_", maxsplit=1)[1]] = value
        return values


# --- ITEMS ---
class ItemCreate(BaseModel):
    title: str
    price: float


class ItemRead(SQLCondition):
    item_id: Optional[int] = None
    title: Optional[str] = None


class ItemUpdate(ItemRead):
    price: Optional[float] = None
    new_title: Optional[str] = None
    new_price: Optional[float] = None


class ItemDelete(ItemRead):
    price: Optional[float] = None


# --- ITEMS ---


# --- ORDERS ---
class OrderCreate(BaseModel):
    user_id: int
    item_id: int


class OrderRead(SQLCondition):
    order_id: Optional[str] = None
    user_id: Optional[int] = None
    item_id: Optional[int] = None


class OrderUpdate(SQLCondition):
    order_id: Optional[str] = None
    new_user_id: Optional[int] = None
    new_item_id: Optional[int] = None


class OrderDelete(SQLCondition):
    order_id: Optional[str] = None


# --- ORDERS ---


# --- USERS ---
class UserCreate(BaseModel):
    username: str


class UserRead(SQLCondition):
    user_id: Optional[int] = None
    username: Optional[str] = None


class UserUpdate(UserRead):
    new_user_id: Optional[int] = None
    new_username: Optional[str] = None


class UserDelete(UserRead): ...


# --- USERS ---
