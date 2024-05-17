#!/usr/bin/python3
""" Client module """

from server.models.person import Person
from server.models.base_model import Base
from sqlalchemy.orm import relationship


class Client(Person, Base):
    """Representation of a Client """
    __tablename__ = 'clients'
    reviews = relationship("Review", backref="client")

    enrolments = relationship("EnrolClient", backref="client")

    def __init__(self, *args, **kwargs):
        """initializes Client"""
        super().__init__(*args, **kwargs)
