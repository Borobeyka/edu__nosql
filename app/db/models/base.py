from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

DeclarativeBase = declarative_base(cls=RepresentableBase)


class Base(DeclarativeBase):
    __abstract__ = True

    def as_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
