""" This module initialize a storage instance """

from server.models.engine.database import DBStorage


storage = DBStorage()
storage.reload()
