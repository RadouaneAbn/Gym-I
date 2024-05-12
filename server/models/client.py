#!/usr/bin/python3
""" holds class User"""

from server.models.person import Person
from server.models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Table

client_gymes = Table('client_gymes', Base.metadata,
                    Column('client_id', String(60),
                           ForeignKey('clients.id', onupdate='CASCADE',
                                      ondelete='CASCADE'), primary_key=True),
                    Column('gym_id', String(60),
                           ForeignKey('gymes.id', onupdate='CASCADE',
                                      ondelete='CASCADE'), primary_key=True))




class Client(Person, Base):
    """Representation of a user """
    __tablename__ = 'clients'
    # gym = ForeignKey('Gym.costumers', nullable=True)
    gymes = relationship("Gym",
                             secondary=client_gymes,
                             viewonly=False)
    reviews = relationship("Review", backref="client")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
