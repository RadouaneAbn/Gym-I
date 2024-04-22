#!/usr/bin/python
""" holds class Gym"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

gym_amenity = Table('gym_amenity', Base.metadata,
                      Column('gum_id', String(60),
                             ForeignKey('gymes.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                                        primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                                        primary_key=True))

class Gym(BaseModel, Base):
    """Representation of Gym """
    __tablename__ = 'gymes'
    name = Column(String(128), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    location = Column(String(256), nullable=False)
    description = Column(String(1024), nullable=True)
    price_by_month = Column(Integer, nullable=False, default=0)
    price_by_year = Column(Integer, nullable=False, default=0)
    reviews = relationship("Review", backref="Gym",
                           cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity",
                             secondary=gym_amenity,
                             viewonly=False)

    def __init__(self, *args, **kwargs):
        """initializes Gym"""
        super().__init__(*args, **kwargs)
