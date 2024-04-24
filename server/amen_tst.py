#!/usr/bin/python3
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.gym import Gym
from models.client import Client
from models.owner import Owner
from models.review import Review
from models import storage
import time


owner = Owner(first_name="radouane",
              last_name="abn",
              email="red@gmail.com",
              password="1234")
owner.save()
city = City(name="safi")
city.save()
amenity = Amenity(name="Wifi")
amenity.save()
owner_id = owner.id
city_id = city.id
location = "Saada"
price_by_month = 20
price_by_year = 0
links = ["1", "2"]
