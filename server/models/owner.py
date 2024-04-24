#!/usr/bin/python3
""" holds class User"""

from server.models.person import Person
from server.models.base_model import Base
from sqlalchemy.orm import relationship
from hashlib import md5


class Owner(Person, Base):
    """Representation of a user """
    __tablename__ = 'owners'
    gym = relationship("Gym", backref="owner")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
