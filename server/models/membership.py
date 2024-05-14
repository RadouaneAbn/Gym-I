#!/usr/bin/python3
""" holds class User"""

from server.models.person import Person
import server.models
from server.models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table, DateTime
from datetime import datetime
import uuid

class EnrolClient(Base):
    """ Representation of the enrolement of a client  """
    __tablename__ = 'enrolments'
    id = Column(String(60), primary_key=True)
    client_id = Column(String(60), ForeignKey("clients.id"), nullable=False)
    gym_id = Column(String(60), ForeignKey("gymes.id"), nullable=False)
    from_date = Column(DateTime, default=datetime.utcnow())
    to_date = Column(DateTime, nullable=False)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        

    @property
    def is_active(self):
        """Calculates if the enrollment is active based on the current date"""
        return self.to_date > datetime.utcnow()
    
    def to_dict(self):
        return {
            "id": self.id,
            "from_date": self.from_date,
            "to_date": self.to_date
        }
    
    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        server.models.storage.new(self)
        server.models.storage.save()
 
    def delete(self):
        """delete the current instance from the storage"""
        server.models.storage.delete(self)