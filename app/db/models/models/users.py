from sqlalchemy import Column, Integer
from sqlalchemy.dialects import postgresql

from app.db.models.base import Base


# fmt: off
class User(Base):
    """Пользователи"""

    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, nullable=False)                         # ID лида
    username = Column(postgresql.VARCHAR(256), nullable=True)                           # Email
# fmt: on
