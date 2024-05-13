from typing import List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


# class ProbaTable(Base):
#     __tablename__ = "users"  # сообщает SQLAlchemy имя таблицы
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True, index=True)
#     description = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True)

class ProbaTable(Base):
    __tablename__ = "users"  # сообщает SQLAlchemy имя таблицы

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)

