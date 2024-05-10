#!/usr/bin/python3
""" Tests for the database """
from server.models.client import Client
from server.models.owner import Owner
from server.models.amenity import Amenity
from server.models.city import City
from server.models.gym import Gym
from server.models.engine.database import DBStorage
from server.models.engine import database
from hashlib import md5
from server.models import storage
import unittest
import inspect
import pep8

amenity_ids = []
amenities_list = []
city_ids = []
client_ids = []
owner_ids = []
gym_ids = []


class DB_storage_check(unittest.TestCase):
    """ Test pycodestyle and documentation of the modules """
    @classmethod
    def setUpClass(cls):
        """ Set up a list of tuples("class_name", class_obj) """
        cls.db_storage_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_DB_storage(self):
        """ Test the pycodestyle of database.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['server/models/engine/database.py'])
        self.assertEqual(result.total_errors, 0,
                         "** database.py: PyCodeStyle Failed !!!")

    def test_pep8_test_DB_storage(self):
        """ Test the pycodestyle of database.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_engine/test_DB.py'])
        self.assertEqual(result.total_errors, 0,
                         "** test_DB.py: PyCodeStyle Failed !!!")

    def test_DB_storage_module_docstring(self):
        """ Test for the presence of docstrings in DB_storage model """
        self.assertIsNot(database.__doc__, None,
                         "No documentation found for DB_storage module")
        self.assertTrue(len(database.__doc__) >= 1,
                        "No documentation found for DB_storage module")

    def test_DB_storage_class_docstring(self):
        """ Test for the presence of docstrings in DB_storage class """
        self.assertIsNot(DBStorage.__doc__, None,
                         "No documentation found for DB_storage class")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "No documentation found for DB_storage class")

    def test_DB_storage_func_docstrings(self):
        """ Test for the presence of docstrings in DB_storage methods """
        for func in self.db_storage_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class Test_1_Create(unittest.TestCase):
    """  """
    amenities = ["Wifi", "Music", "TV", "Pool"]
    cities = ["Casablanca", "Safi", "Wejda", "Nador"]
    clients = [
        {"first_name": "first one", "last_name": "last one",
         "email": "one@client.com", "password": "1234"},
        {"first_name": "first two", "last_name": "last two",
         "email": "two@client.com", "password": "1234"},
        {"first_name": "first three", "last_name": "last three",
         "email": "three@client.com", "password": "1234"},
        {"first_name": "first foor", "last_name": "last foor",
         "email": "foor@client.com", "password": "1234"}
        ]
    owners = [
        {"first_name": "first one", "last_name": "last one",
         "email": "one@owner.com", "password": "1234"},
        {"first_name": "first two", "last_name": "last two",
         "email": "two@owner.com", "password": "1234"},
        {"first_name": "first three", "last_name": "last three",
         "email": "three@owner.com", "password": "1234"},
        {"first_name": "first foor", "last_name": "last foor",
         "email": "foor@owner.com", "password": "1234"}
        ]
    classes = {"Client": Client,
               "Gym": Gym,
               "City": City,
               "Amenity": Amenity,
               "Owner": Owner}

    def test_1_amenity_create(self):
        for amenity_name in self.amenities:
            amenity = Amenity(name=amenity_name)
            amenity.save()
            amenities_list.append(amenity)
            amenity_ids.append(amenity.id)

        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            self.assertIsNotNone(amenity)
            self.assertIsInstance(amenity, Amenity)

    def test_2_city_create(self):
        for city_name in self.cities:
            city = City(name=city_name)
            city.save()
            city_ids.append(city.id)

        for city_id in city_ids:
            city = storage.get(City, city_id)
            self.assertIsNotNone(city)
            self.assertIsInstance(city, City)

    def test_3_client_create(self):
        for client in self.clients:
            client = Client(**client)
            client.save()
            client_ids.append(client.id)

        for client_id in client_ids:
            client = storage.get(Client, client_id)
            self.assertIsNotNone(client)
            self.assertIsInstance(client, Client)

    def test_4_owner_create(self):
        for owner in self.owners:
            owner = Owner(**owner)
            owner.save()
            owner_ids.append(owner.id)

        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            self.assertIsNotNone(owner)
            self.assertIsInstance(owner, Owner)

    def test_5_gym_create(self):
        for i in range(4):
            gym_info = {
                "name": f"gym-{i + 1}",
                "city_id": city_ids[i],
                "owner_id": owner_ids[i],
                "location": f"location-{i + 1}",
                "description": f"desc-{i + 1}",
                "price_by_month": 20 * (i + 1),
                "price_by_year": 20 * (i + 1) * 10,
                "profile_picture": f"link to picture {i + 1}",
                "amenities": amenities_list,
                "links": ["link-1", "link-2"]
            }
            gym = Gym(**gym_info)
            gym.save()
            gym_ids.append(gym.id)

        for i, gym_id in enumerate(gym_ids):
            gym = storage.get(Gym, gym_id)
            self.assertIsNotNone(gym)
            self.assertIsInstance(gym, Gym)
            self.assertEqual(getattr(gym, "name", None), f"gym-{i + 1}")
            self.assertEqual(getattr(gym, "city_id", None), city_ids[i])
            self.assertEqual(getattr(gym, "owner_id", None), owner_ids[i])
            self.assertEqual(getattr(gym, "location", None),
                             f"location-{i + 1}")
            self.assertEqual(getattr(gym, "description", None),
                             f"desc-{i + 1}")
            self.assertEqual(getattr(gym, "price_by_month", None),
                             20 * (i + 1))
            self.assertEqual(getattr(gym, "price_by_year", None),
                             20 * (i + 1) * 10)
            self.assertEqual(getattr(gym, "profile_picture", None),
                             f"link to picture {i + 1}")
            self.assertEqual(getattr(gym, "amenities", None), amenities_list)
            self.assertEqual(getattr(gym, "links", None), ["link-1", "link-2"])


class Test_2_Update(unittest.TestCase):
    name_u = "name update"
    f_name_u = "first name update"
    l_name_u = "last name update"
    email_u = "test@mail.com"
    password_u = "test"
    city_u = ""
    owner_u = ""
    location_u = "location update test"
    description_u = "description update test"
    price_by_month_u = 111
    price_by_year = 101
    amenities_u = []
    links_u = ["links", "update", "test"]

    def test_amenity_update(self):
        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            amenity.name = self.name_u
            amenity.save()

        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            self.assertEqual(amenity.name, self.name_u)

    def test_city_update(self):
        for city_id in city_ids:
            city = storage.get(City, city_id)
            city.name = self.name_u
            city.save()

        for city_id in city_ids:
            city = storage.get(City, city_id)
            self.assertEqual(city.name, self.name_u)

    def test_client_update(self):
        for client_id in client_ids:
            client = storage.get(Client, client_id)
            client.first_name = self.f_name_u
            client.last_name = self.l_name_u
            client.email = self.email_u
            client.password = self.password_u
            client.save()

        for client_id in client_ids:
            client = storage.get(Client, client_id)
            self.assertEqual(client.first_name, self.f_name_u)
            self.assertEqual(client.last_name, self.l_name_u)
            self.assertEqual(client.email, self.email_u)
            self.assertEqual(client.password,
                             md5(self.password_u.encode()).hexdigest())

    def test_owner_update(self):
        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            owner.first_name = self.f_name_u
            owner.last_name = self.l_name_u
            owner.email = self.email_u
            owner.password = self.password_u
            owner.save()

        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            self.assertEqual(owner.first_name, self.f_name_u)
            self.assertEqual(owner.last_name, self.l_name_u)
            self.assertEqual(owner.email, self.email_u)
            self.assertEqual(owner.password,
                             md5(self.password_u.encode()).hexdigest())

    def test_gym_update(self):
        self.city_u = city_ids[0]
        self.owner_u = owner_ids[0]
        self.amenities_u.append(amenities_list[0])
        for gym_id in gym_ids:
            gym = storage.get(Gym, gym_id)
            gym.name = self.name_u
            gym.owner_id = self.owner_u
            gym.city_id = self.city_u
            gym.location = self.location_u
            gym.description = self.description_u
            gym.price_by_month = self.price_by_month_u
            gym.price_by_year = self.price_by_year
            gym.amenities = self.amenities_u
            gym.links = self.links_u
            gym.save()

        for gym_id in gym_ids:
            gym = storage.get(Gym, gym_id)
            self.assertEqual(gym.name, self.name_u)
            self.assertEqual(gym.owner_id, self.owner_u)
            self.assertEqual(gym.city_id, self.city_u)
            self.assertEqual(gym.location, self.location_u)
            self.assertEqual(gym.description, self.description_u)
            self.assertEqual(gym.price_by_month, self.price_by_month_u)
            self.assertEqual(gym.price_by_year, self.price_by_year)
            self.assertEqual(gym.amenities, self.amenities_u)
            self.assertEqual(gym.links, self.links_u)


class Test_3_Delete(unittest.TestCase):

    def test_1_gym_delete(self):
        for gym_id in gym_ids:
            gym = storage.get(Gym, gym_id)
            gym.delete()

        storage.save()

        for gym_id in gym_ids:
            gym = storage.get(Gym, gym_id)
            self.assertIsNone(gym)

    def test_2_owner_delete(self):
        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            owner.delete()

        storage.save()

        for owner_id in owner_ids:
            owner = storage.get(Owner, owner_id)
            self.assertIsNone(owner)

    def test_3_client_delete(self):
        for client_id in client_ids:
            client = storage.get(Client, client_id)
            client.delete()

        storage.save()

        for client_id in client_ids:
            client = storage.get(Client, client_id)
            self.assertIsNone(client)

    def test_4_amenity_delete(self):
        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            amenity.delete()

        storage.save()

        for amenity_id in amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            self.assertIsNone(amenity)

    def test_5_city_delete(self):
        for city_id in city_ids:
            city = storage.get(City, city_id)
            city.delete()

        storage.save()

        for city_id in city_ids:
            city = storage.get(City, city_id)
            self.assertIsNone(city)
