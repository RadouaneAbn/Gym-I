#!/usr/bin/python3
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.gym import Gym
from models.client import Client
from models.owner import Owner
from models.review import Review
from models import storage
from sys import argv as av
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


def create_gymes(n=1000):
    for i in range(n):
        new_gym = Gym(name=f"{i + 1}",
                    owner_id=owner_id,
                    city_id=city_id,
                    location=location,
                    description= f"description of {i + 1}",
                    price_by_month=price_by_month,
                    price_by_year=price_by_year,
                    amenities=[amenity],
                    links=links)
        print(i + 1, new_gym.id)
        new_gym.save()


id = "b90ac35f-3c6c-4357-880d-3917e2b506a0"
def get_q():
    start = time.time()
    inst = storage.get(Gym, id)
    end = time.time()
    print("time to query [" + inst.id + "] is:", end - start)


def get_a():
    start = time.time()
    all_inst = storage.all(Gym).values()
    for inst in all_inst:
        if inst.id == id:
            end = time.time()
            print("time to query [" + inst.id + "] is:", end - start)
            break

if len(av) > 1:
    create_gymes(int(av[1]))
else:
    create_gymes()

# print("##########################")
# get_a()
# print("##########################")
# get_q()
# print("##########################")
