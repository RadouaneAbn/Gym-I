#!/usr/bin/python3
""" Owner module """
from server.models.person import Person
from server.models.base_model import Base
from sqlalchemy.orm import relationship


class Owner(Person, Base):
    """Representation of a Owner """
    __tablename__ = 'owners'
    gym = relationship("Gym", backref="owner")

    def __init__(self, *args, **kwargs):
        """initializes Owner """
        super().__init__(*args, **kwargs)
