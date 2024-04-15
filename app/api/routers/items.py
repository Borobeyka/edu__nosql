from fastapi import APIRouter, Depends
from fastapi_redis_cache import cache

from app.api.schemas import schema
from app.db.base import NewSession, delete_sql, insert_sql, select_sql, update_sql
from app.db.models import Item

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("/")
def items_create(data: schema.ItemCreate):
    query = insert_sql(
        "items",
        values=data.model_dump(),
        returns="*",
    )
    with NewSession() as db:
        row = db.execute(query).fetchone()
        db.commit()
    return Item(**row)


@router.get("/")
@cache(expire=30)
def items_read(data: schema.ItemRead = Depends()):
    query = select_sql(
        "items",
        where=data.where(),
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [Item(**row) for row in rows]


@router.put("/")
def items_update(data: schema.ItemUpdate):
    query = update_sql("items", values=data.values(), where=data.where(), returns="*")
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [Item(**row) for row in rows]


@router.delete("/")
def items_delete(data: schema.ItemDelete):
    query = delete_sql(
        "items",
        where=data.where(),
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [Item(**row) for row in rows]
