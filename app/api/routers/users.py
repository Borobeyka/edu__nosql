from fastapi import APIRouter, Depends
from fastapi_redis_cache import cache

from app.api.schemas import schema
from app.db.base import NewSession, delete_sql, insert_sql, select_sql, update_sql
from app.db.models import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def users_create(data: schema.UserCreate):
    query = insert_sql("users", values=data.model_dump(), returns="*")
    with NewSession() as db:
        row = db.execute(query).fetchone()
        db.commit()
    return User(**row)


@router.get("/")
@cache(expire=30)
def users_read(data: schema.UserRead = Depends()):
    query = select_sql(
        "users",
        where=data.where(),
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [User(**row) for row in rows]


@router.put("/")
def users_update(data: schema.UserUpdate):
    query = update_sql(
        "users",
        values=data.values(),
        where=data.where(),
        returns="*",
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [User(**row) for row in rows]


@router.delete("/")
def users_delete(data: schema.UserDelete):
    query = delete_sql(
        "users",
        where=data.where(),
    )
    with NewSession() as db:
        rows = db.execute(query).fetchall()
        db.commit()
    return [User(**row) for row in rows]
