#!/usr/bin/python3
""" holds class User"""

from server.models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from hashlib import md5
from server.models.engine.secure import hash_password
from sqlalchemy.dialects.postgresql import ARRAY


class Person(BaseModel):
    """Representation of a user """
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    profile_picture = Column(String(128), nullable=True)
    profile_picture_original = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = hash_password(value)
        super().__setattr__(name, value)

    @property
    def get_profile_picture(self):
        return self.profile_picture or "https://i.ibb.co/bmSHH9j/no-profile-128.png"

    @property
    def get_profile_picture_original(self):
        return self.profile_picture_original or "https://i.ibb.co/whS5nPK/no-pic.png"