#!/usr/bin/python3
from server.models.amenity import Amenity
from server.models.base_model import BaseModel
from server.models.city import City
from server.models.gym import Gym
from server.models.client import Client
from server.models.owner import Owner
from server.models.review import Review
from server.models import storage
import time

gymes_list = []
am = storage.get(Amenity, "31ff1ce9-f0a5-4b60-9557-4b0b14b34730")

for i in range(10000):
    gym = Gym(name=f"test gym-{i + 1}",
              city_id="c77d94e6-9f82-4db1-8298-e69c64554cd4",
              owner_id="75fddd11-54d6-4db5-83b6-5c8e47fe2642",
              location="local",
              description="By drawing on a fundamental description of cause and effect found in Einstein’s theory of special relativity, researchers from Imperial College London have come up with a way to help AIs make better guesses too.",
              price_by_month = 100,
              price_by_year=0,
              amenities = [am],
              links=[])
    gym.save()
    print(f"\r {i}", end="")

print("all gymes created")

def lunch_test():
    try:
        for i in range(1, 1000):
            offset = (i - 1) * 10
            limit = offset + 10

            st = time.time()
            all_gym = storage.all_2(Gym)[offset:limit]
            en = time.time()

            st_2 = time.time()
            all_gym = storage.get_page(Gym, i)
            en_2 = time.time()
            n = en - st
            m = en_2 - st_2
            if n > m:
                print(f"[{i}]: {n} > {m}")
            elif n < m:
                print(f"[{i}]: {n} < {m}")
            else:
                print(f"[{i}]: {n} = {m}")
    except Exception:
        pass

def getpage(page = 1):
    # page = 400
    offset = (page - 1) * 10
    limit = offset + 10

    st = time.time()
    all_gym = storage.all_2(Gym)[offset:limit]
    en = time.time()
    for gym in all_gym:
        print(gym.name)
    print("######################")
    st2 = time.time()
    all_gym = storage.get_page(Gym, page)
    en2 = time.time()
    for gym in all_gym:
        print(gym.name)
    print(f"[{page}]: {en - st} <--> {en2 - st2}")

if __name__ == "__main__":
    while True:
        n = int(input("n = "))
        getpage(n)
    #     if input("quit? ") == "":
    #         lunch_test()
    #     else:
    #         for gym in gymes_list:
    #             gym.delete()
    #             storage.save() 
    #         print("all gymes deleted")
    #         break
            