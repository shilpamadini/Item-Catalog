#!/usr/bin/env python
"""Python code to create itemcatalog.db."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    """Python object for database table user."""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Catalog(Base):
    """Python object for database table Catalog."""

    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    catalog_name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Returns data in a serializeable format."""
        return {
            'catalog_name': self.catalog_name,
            'id': self.id,
        }


class CatalogItem(Base):
    """Python object for the database table catalog_item."""

    __tablename__ = 'catalog_item'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(80), nullable=False)
    description = Column(String(1000))
    catalog_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Returns data in a serializeable format."""
        return {
            'item_name': self.item_name,
            'description': self.description,
            'id': self.id
        }


engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)
