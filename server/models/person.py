#!/usr/bin/python3
""" Person module """
from collections.abc import Iterable
from server.models.base_model import BaseModel
from sqlalchemy import Column, String
from server.models.engine.secure import hash_password


class Person(BaseModel):
    """ Representation of a Person """
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    profile_picture = Column(String(128), nullable=True)
    profile_picture_original = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """ initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """ encrypts the password """
        if name == "password":
            value = hash_password(value)
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        """ This method gets the value of an attribute """
        value = super().__getattribute__(name)

        if not value:
            if name == "profile_picture_original":
                value = "https://i.ibb.co/whS5nPK/no-pic.png"
            if name == "profile_picture":
                value = "https://i.ibb.co/bmSHH9j/no-profile-128.png"

        return value
