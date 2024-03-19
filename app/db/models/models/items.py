from sqlalchemy import Column, Integer
from sqlalchemy.dialects import postgresql

from app.db.models.base import Base


# fmt: off
class Item(Base):
    """Товары"""

    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, nullable=False)                         # ID товара
    title = Column(postgresql.VARCHAR(256))                                             # Наименование
    price = Column(postgresql.NUMERIC(16, 2))                                           # Стоимость
# fmt: on
