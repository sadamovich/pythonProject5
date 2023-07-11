from sqlalchemy import Column, VARCHAR, TEXT, INT, ForeignKey

from .database import Base


class Category(Base):
    name = Column(VARCHAR(64), nullable=False, unique=True, index=True)
    slug = Column(VARCHAR(64), nullable=False, unique=True, index=True)


class Runner(Base):
    name = Column(VARCHAR(32), nullable=False)
    surname = Column(VARCHAR(32), nullable=False)
    description = Column(TEXT, nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)
