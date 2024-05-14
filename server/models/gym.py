#!/usr/bin/python
""" holds class Gym"""
from server.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
# from server.models.amenity import Amenity
from server.models.membership import EnrolClient
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

gym_amenity = Table('gym_amenity', Base.metadata,
                    Column('gym_id', String(60),
                           ForeignKey('gymes.id', onupdate='CASCADE',
                                      ondelete='CASCADE'), primary_key=True),
                    Column('amenity_id', String(60),
                           ForeignKey('amenities.id', onupdate='CASCADE',
                                      ondelete='CASCADE'), primary_key=True))


class Gym(BaseModel, Base):
    """Representation of Gym """
    __tablename__ = 'gymes'
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    owner_id = Column(String(60), ForeignKey('owners.id'), nullable=False)
    location = Column(String(256), nullable=False)
    description = Column(String(1024), nullable=True)
    price_by_month = Column(Integer, nullable=False, default=0)
    price_by_year = Column(Integer, nullable=False, default=0)
    profile_picture = Column(String(256), nullable=False)
    reviews = relationship("Review", backref="gym",
                           cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity",
                             secondary=gym_amenity,
                             viewonly=False)
    links = Column(ARRAY(String), nullable=True)

    enrolments = relationship("EnrolClient", backref="gym")

    def __init__(self, *args, **kwargs):
        """initializes Gym"""
        super().__init__(*args, **kwargs)
