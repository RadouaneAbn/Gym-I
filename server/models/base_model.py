#!/usr/bin/python3
"""
Contains class BaseModel
"""
from datetime import datetime
import server.models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def set_datetime(self, date_time):
        """ This function sets the time if an attribute created_at/updated_at
            is found or sets it to now """
        if date_time and isinstance(date_time, str):
            return datetime.strptime(date_time, time)
        return datetime.now()

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = self.set_datetime(kwargs.get("created_at"))
            self.updated_at = self.set_datetime(kwargs.get("updated_at"))
            self.id = kwargs.get("id", str(uuid.uuid4()))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        server.models.storage.new(self)
        server.models.storage.save()

    def to_dict(self, show_password=False, pop=[]):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        for item in pop:
            new_dict.pop(item, None)

        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        # print(self)
        if new_dict["__class__"] in ["Client", "Owner"]:
            new_dict["profile_picture"] = self.get_profile_picture
            new_dict["profile_picture_original"] = self.\
                get_profile_picture_original

        new_dict.pop("_sa_instance_state", None)
        new_dict.pop("password", None)
        return new_dict

    def delete(self):
        """ delete the current instance from the database """
        server.models.storage.delete(self)
