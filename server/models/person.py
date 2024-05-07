#!/usr/bin/python3
""" holds class User"""

from server.models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5
from server.models.engine.secure import hash_password


class Person(BaseModel):
    """Representation of a user """
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    profile_picture = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = hash_password(value)
        super().__setattr__(name, value)
