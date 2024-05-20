#!/usr/bin/python
""" City module """
from server.models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    gymes = relationship("Gym",
                         backref="cities",
                         cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
