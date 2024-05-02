#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import server.models
from server.models.amenity import Amenity
from server.models.city import City
from server.models.gym import Gym
from server.models.review import Review
from server.models.client import Client
from server.models.owner import Owner
from server.models.city import City
from server.models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv


load_dotenv()

classes = {"Client": Client, "Gym": Gym, "City": City,
           "Amenity": Amenity, "Review": Review, "Owner": Owner}


class DBStorage:
    """interaacts with the POST database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        GYMNI_POST_USER = getenv('GYMNI_POST_USER')
        GYMNI_POST_PWD = getenv('GYMNI_POST_PWD')
        GYMNI_POST_HOST = getenv('GYMNI_POST_HOST')
        GYMNI_POST_DB = getenv('GYMNI_POST_DB')
        GYMNI_ENV = getenv('GYMNI_ENV')
        self.__engine = create_engine(
            'postgresql+psycopg2://{}:{}@{}/{}'.format(
                GYMNI_POST_USER,
                GYMNI_POST_PWD,
                GYMNI_POST_HOST,
                GYMNI_POST_DB))

        if GYMNI_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def clean(self):
        """ This funtion deletes all tables from the database and
            then create them again
        """
        Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)


    def all_list(self, cls=None):
        """query on the current database session"""
        return (self.__session.query(cls).all())

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(server.models.storage.all(clas).values())
        else:
            count = len(server.models.storage.all(cls).values())
        return count

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        inst = self.__session.query(cls).filter(
            cls.id == id
        ).first()
        return inst

    def email_exists(self, cls, email):
        """ This method checks if the user email is already in the database
            'checks for duplicates'
        """
        inst = self.__session.query(cls).filter(
            cls.email == email
        ).first()
        if inst:
            return False
        return True

    def get_page(self, cls, page = 1):
        offset = (page - 1) * 10
        limit = 10
        page_insts = self.__session.query(cls)\
            .offset(offset).limit(limit).all()
        return page_insts

    def gymes_in_cities(self, city_ids):
        all_gymes = self.__session.query(Gym).filter(
            Gym.city_id.in_(city_ids)
        ).all()
        return all_gymes
    
    def get_user(self, cls, email):
        inst = self.__session.query(cls).filter(
            cls.email == email
        ).first()
        return inst