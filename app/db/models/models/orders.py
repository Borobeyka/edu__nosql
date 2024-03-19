from sqlalchemy import Column, ForeignKey, Integer

from app.db.models.base import Base


# fmt: off
class Order(Base):
    """Заказы"""

    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, nullable=False)                        # ID заказа
    user_id = Column(Integer, ForeignKey(column="users.user_id",
                     onupdate="RESTRICT", ondelete="RESTRICT"))                         # ID пользователя
    item_id = Column(Integer, ForeignKey(column="items.item_id",
                     onupdate="RESTRICT", ondelete="RESTRICT"))                         # ID товара
# fmt: on
