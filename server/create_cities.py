#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import models
from models.city import City
from models.gym import Gym
from models.client import Client
from models.owner import Owner
from models.review import Review
from models.amenity import Amenity

def run():
    moroccan_cities = [
        "Casablanca", "Rabat", "Fes", "Marrakech", "Tangier", "Agadir", "Meknes", "Oujda",
        "Kenitra", "Tetouan", "Safi", "Mohammedia", "Khouribga", "Beni Mellal", "El Jadida", "Taza",
        "Nador", "Settat", "Larache", "Ksar El Kebir", "Essaouira", "Taounate", "Sidi Kacem",
        "Sidi Slimane", "Chefchaouen", "Azrou", "Al Hoceima", "Errachidia", "Zagora", "Ouarzazate"
        ]
    for city_name in moroccan_cities:
        new_city = City(name=city_name)
        new_city.save()

def delete_cities():
    cities = models.storage.all(City).values()
    for city in cities:
        models.storage.delete(city)
    models.storage.save()

def list_cities():
    for city in models.storage.all(City).values():
        print(f"{city.id} {city.name}")

def list_amenities():
    for am in models.storage.all(Amenity).values():
        print(f"{am.id} {am.name}")

def list_owners():
    for owner in models.storage.all(Owner).values():
        print(f"{owner.id} {owner.first_name}")

if __name__ == "__main__":
    # delete_cities()
    # run()
    list_cities()
    print()
    list_amenities()
    print()
    list_owners()