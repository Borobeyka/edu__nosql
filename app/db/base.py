from logging import getLogger
from typing import Dict, List, Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from app.config.secrets import ENV
from app.service.json import json

# fmt: off

log = getLogger()


DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username=ENV.get("PGPOOL_POSTGRES_USERNAME"),
    password=ENV.get("PGPOOL_POSTGRES_PASSWORD"),
    host=ENV.get("PGPOOL_HOST"),
    port=ENV.get("PGPOOL_PORT"),
    database=ENV.get("POSTGRESQL_DATABASE"),
)
REAL_DATABASE_PARAMS = {
    "pool_pre_ping": True,
    "echo": False,
    "pool_size": 10,
    "max_overflow": 50,
    #  echo_pool: 'debug',
}

engine = create_engine(
    DATABASE_URL,
    **REAL_DATABASE_PARAMS,
    json_serializer=json.dumps,
    json_deserializer=json.loads,
)
NewSession = sessionmaker(bind=engine)


def select_sql(
    table: str,
    *,
    fields: Optional[List[str]] = None,
    where: Optional[Dict[str, str | int | float]] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Optional[str]:
    if not table:
        return None
    query = [
        "SELECT",
        ", ".join(fields) if fields else "*",
        f"FROM {table}",
        "WHERE " + " AND ".join([f"{field}={value!r}" for field, value in where.items() if value]) if where else None,
        f"LIMIT {limit}" if limit else None,
        f"OFFSET {offset}" if offset else None,
    ]
    return " ".join([cmd for cmd in query if cmd])


def insert_sql(
    table: str,
    *,
    values: Dict[str, str | int | float],
    ignore: bool = False,
    conflict_fields: Optional[List[str]] = None,
    conflict_fields_update: Optional[Dict[str, str | int | float]] = None,
    returns: List[str] | str = "*"
) -> Optional[str]:
    if not table or not values:
        return None
    query = [
        f"INSERT INTO {table}",
        f"({", ".join(values.keys())})",
        f"VALUES ({", ".join([f"{value!r}" for value in values.values()])})",
        (
            f"ON CONFLICT ({", ".join(conflict_fields)}) DO UPDATE SET {", ".join([f"{field}={value!r}" for field, value in conflict_fields_update.items()])}" if conflict_fields_update and conflict_fields else
            f"ON CONFLICT ({", ".join(conflict_fields)}) DO NOTHING" if conflict_fields else
            "ON CONFLICT DO NOTHING" if ignore else None
        ),
        (
            f"RETURNING {", ".join(returns)}" if isinstance(returns, list)
            else f"RETURNING {returns}" if isinstance(returns, str) else None
        ),
    ]
    return " ".join([cmd for cmd in query if cmd])


def delete_sql(
    table: str,
    *,
    where: Optional[Dict[str, str | int | float]] = None,
    returns: List[str] | str = "*"
):
    if not table:
        return None
    query = [
        f"DELETE FROM {table}",
        "WHERE " + " AND ".join([f"{field}={value!r}" for field, value in where.items() if value]) if where else None,
        (
            f"RETURNING {", ".join(returns)}" if isinstance(returns, list)
            else f"RETURNING {returns}" if isinstance(returns, str) else None
        ),
    ]
    return " ".join([cmd for cmd in query if cmd])


def update_sql(
    table: str,
    *,
    values: Dict[str, str | int | float],
    where: Optional[Dict[str, str | int | float]] = None,
    returns: List[str] | str = "*"
):
    if not table or not values:
        return None
    query = [
        f"UPDATE {table}",
        "SET " + ", ".join([f"{field}={value!r}" for field, value in values.items()]) if values else None,
        "WHERE " + " AND ".join([f"{field}={value!r}" for field, value in where.items() if value]) if where else None,
        (
            f"RETURNING {", ".join(returns)}" if isinstance(returns, list)
            else f"RETURNING {returns}" if isinstance(returns, str) else None
        ),
    ]
    return " ".join([cmd for cmd in query if cmd])
