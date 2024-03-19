from fastapi import APIRouter, Depends

from app.api.schemas import schema
from app.db.base import NewSession, delete_sql, insert_sql, select_sql, update_sql
from app.db.models import Order

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def orders_create(data: schema.OrderCreate):
    query = insert_sql(
        "orders",
        values=data.model_dump(),
    )
    with NewSession() as db:
        row = db.execute(query).fetchone()
        db.commit()
    return Order(**row)


@router.get("/")
def orders_read(data: schema.OrderRead = Depends()):
    query = select_sql(
        "orders",
        where=data.where(),
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [Order(**row) for row in rows]


@router.put("/")
def orders_update(data: schema.OrderUpdate):
    query = update_sql(
        "orders",
        values=data.values(),
        where=data.where(),
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [Order(**row) for row in rows]


@router.delete("/")
def orders_delete(data: schema.OrderDelete):
    query = delete_sql(
        "orders",
        where=data.where(),
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [Order(**row) for row in rows]
