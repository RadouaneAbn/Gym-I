#!/usr/bin/python3
""" Tests for the database """
from server.models.client import Client
from server.models.owner import Owner
from server.models.amenity import Amenity
from server.models.city import City
from server.models.gym import Gym
from server.models import storage
import unittest


unittest.TestLoader.sortTestMethodsUsing = None
amenity_ids = []
city_ids = []
client_ids = []
owner_ids = []
gym_ids = []
classes = {"Client": Client,
           "Gym": Gym,
           "City": City,
           "Amenity": Amenity,
           "Owner": Owner}
owners = [
    {"first_name": "first one", "last_name": "last one",
        "email": "one@owner.com", "password": "1234" },
    {"first_name": "first two", "last_name": "last two",
        "email": "two@owner.com", "password": "1234" },
    {"first_name": "first three", "last_name": "last three",
        "email": "three@owner.com", "password": "1234" },
    {"first_name": "first foor", "last_name": "last foor",
        "email": "foor@owner.com", "password": "1234" }
    ]
clients = [
    {"first_name": "first one", "last_name": "last one",
        "email": "one@client.com", "password": "1234" },
    {"first_name": "first two", "last_name": "last two",
        "email": "two@client.com", "password": "1234" },
    {"first_name": "first three", "last_name": "last three",
        "email": "three@client.com", "password": "1234" },
    {"first_name": "first foor", "last_name": "last foor",
        "email": "foor@client.com", "password": "1234" }
    ]
amenities = ["Wifi", "Music", "TV", "Pool"]
cities = ["Casablanca", "Safi", "Wejda", "Nador"]


class TestCreateAmenity(unittest.TestCase):
    """  """

    def test_amenity_create(self):
        for amenity_name in amenities:
            amenity = Amenity(name=amenity_name)
            amenity.save()
            amenity_ids.append(amenity.id)
        
        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            self.assertIsNotNone(amenity)
            self.assertIsInstance(amenity, Amenity)


class TestCreateCity(unittest.TestCase):

    def test_city_create(self):
        for city_name in cities:
            city = City(name=city_name)
            city.save()
            city_ids.append(city.id)
        
        for city_id in city_ids:
            city = storage.get(City, city_id)
            self.assertIsNotNone(city)
            self.assertIsInstance(city, City)


class TestCreateClient(unittest.TestCase):

    def test_client_create(self):
        for client in clients:
            client = Client(**client)
            client.save()
            client_ids.append(client.id)
        
        for client_id in client_ids:
            client = storage.get(Client, client_id)
            self.assertIsNotNone(client)
            self.assertIsInstance(client, Client)

class TestCreateOwner(unittest.TestCase):

    def test_owner_create(self):
        for owner in owners:
            owner = Owner(**owner)
            owner.save()
            owner_ids.append(owner.id)
        
        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            self.assertIsNotNone(owner)
            self.assertIsInstance(owner, Owner)


class TestCreateGym(unittest.TestCase):

    def test_gym_create(self):
        for i in range(1, 5):
            gym_info = {
                "name": f"gym-{i}",
                "city_id": city_ids[i - 1],
                "owner_id": owner_ids[i - 1],
                "location": f"location-{i}",
                "description": f"desc-{i}",
                "price_by_month": 20 * i,
                "price_by_year": 20 * 1 * 10,
                "profile_picture": f"link to picture {i}",
                "amenities": amenity_ids,
                "links": []
            }
            gym = Gym(**gym_info)
            gym.save()
            gym_ids.append(gym.id)

        for gym_id in gym_ids:
            gym = storage.get(Gym, gym_id)
            self.assertIsNotNone(gym)
            self.assertIsInstance(gym, Gym)


class TestDelete(unittest.TestCase):

    def test_owner_delete(self):
        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            owner.delete()
        
        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            self.assertIsNone(owner)

    def test_client_delete(self):
        for client_id in client_ids:
            client = storage.get(Client, client_id)
            client.delete()
        
        for client_id in client_ids:
            client = storage.get(Client, client_id)
            self.assertIsNone(client)

    def test_gym_delete(self):
        for gym_id in gym_ids:
            gym = storage.get(Gym, gym_id)
            gym.delete()
        
        for gym_id in gym_ids:
            gym = storage.get(Gym, gym_id)
            self.assertIsNone(gym)

    def test_amenity_delete(self):
        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            amenity.delete()
        
        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            self.assertIsNone(amenity)

    def test_city_delete(self):
        for city_id in city_ids:
            city = storage.get(City, city_id)
            city.delete()
        
        for city_id in city_ids:
            city = storage.get(City, city_id)
            self.assertIsNone(city)