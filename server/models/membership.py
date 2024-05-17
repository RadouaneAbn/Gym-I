#!/usr/bin/python3
""" EnrolClient module """
import server.models
from server.models.base_model import Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from datetime import datetime


class EnrolClient(Base):
    """ A class that enrols a client int a gym """
    __tablename__ = 'enrolments'
    payment_id = Column(String(60), primary_key=True)
    client_id = Column(String(60), ForeignKey("clients.id"), nullable=False)
    gym_id = Column(String(60), ForeignKey("gymes.id"), nullable=False)
    from_date = Column(DateTime, default=datetime.utcnow())
    to_date = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        """ Initializes a EnrolClient instance """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    @property
    def is_active(self):
        """ checkes if the enrollment is active based on the current date"""
        today = datetime.utcnow()
        return self.to_date >= today and self.from_date <= today

    def to_dict(self):
        """ Returns a dictionary representation of the instance """
        return {
            "id": self.id,
            "from_date": self.from_date,
            "to_date": self.to_date
        }

    def __str__(self):
        """String representation of the EnrolClient class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """ saves a instance in the database """
        self.updated_at = datetime.now()
        server.models.storage.new(self)
        server.models.storage.save()

    def delete(self):
        """delete the current instance from the storage"""
        server.models.storage.delete(self)
