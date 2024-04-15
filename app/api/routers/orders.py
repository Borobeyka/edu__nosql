from fastapi import APIRouter, Depends
from fastapi_redis_cache import cache

from app.api.schemas import schema
from app.db.base import CassandraSession
from app.db.models import Order

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/")
def orders_create(data: schema.OrderCreate):
    data = data.model_dump()
    with CassandraSession() as db:
        db.execute(f"INSERT INTO orders (order_id, user_id, item_id) VALUES (uuid(), {data["user_id"]}, {data["item_id"]});")
    return "ok"


@router.get("/")
@cache(expire=30)
def orders_read(data: schema.OrderRead = Depends()):
    query = "SELECT * FROM orders"
    if data.where():
        query += f"WHERE {"AND ".join(f"{field}={value}" for field, value in data.where().items())}"
    with CassandraSession() as db:
        rows = db.execute(query).all()
    return [Order(**row) for row in rows]


@router.put("/")
def orders_update(data: schema.OrderUpdate):
    query = "UPDATE orders SET "
    query += f"{", ".join([f"{field}={value}" for field, value in data.values().items()])}"
    query += f" WHERE {", ".join([f"{field}={value}" for field, value in data.where().items()])}"
    with CassandraSession() as db:
        db.execute(query)
    return "ok"


@router.delete("/")
def orders_delete(data: schema.OrderDelete):
    query = "DELETE FROM orders"
    query += f" WHERE {", ".join([f"{field}={value}" for field, value in data.where().items()])}"
    with CassandraSession() as db:
        db.execute(query)
    return "ok"
