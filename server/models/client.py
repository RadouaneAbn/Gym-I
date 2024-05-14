#!/usr/bin/python3
""" holds class User"""

from server.models.person import Person
from server.models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table

# Many-to-Many Relationship:

class Client(Person, Base):
    """Representation of a user """
    __tablename__ = 'clients'
    reviews = relationship("Review", backref="client")

    enrolments = relationship("EnrolClient", backref="client")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
