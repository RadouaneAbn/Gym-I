#!/usr/bin/python

from hashlib import md5
from server.models.client import Client
from server.models import storage

class Hash:
    def hash_pwd(self, password):
        return md5(password.encode()).hexdigest()
    
    def validate_pwd(pwd: str, client_pwd: str):
        """ compare a password with a hashed password """
        hashed_pwd = md5(pwd.encode()).hexdigest()
        return (hashed_pwd == client_pwd)
        