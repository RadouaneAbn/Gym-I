#!/usr/bin/python3
from server.models.client import Client
from server.models.base_model import BaseModel
from server.models.person import Person
from server.models import client
from hashlib import md5
import unittest
import inspect
import pep8


class Client_check(unittest.TestCase):
    """ Test pycodestyle and documentation of the modules """
    @classmethod
    def setUpClass(cls):
        """ Set up a list of tuples("class_name", class_obj) """
        cls.client_f = inspect.getmembers(Client, inspect.isfunction)

    def test_pep8_client(self):
        """ Test the pycodestyle of client.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['server/models/client.py'])
        self.assertEqual(result.total_errors, 0,
                         "** client.py: PyCodeStyle Failed !!!")

    def test_pep8_test_client(self):
        """ Test the pycodestyle of test_client.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_client.py'])
        self.assertEqual(result.total_errors, 0,
                         "** test_client.py: PyCodeStyle Failed !!!")

    def test_client_module_docstring(self):
        """ Test for the presence of docstrings in client model """
        self.assertIsNot(client.__doc__, None,
                         "No documentation found for client module")
        self.assertTrue(len(client.__doc__) >= 1,
                        "No documentation found for client module")

    def test_client_class_docstring(self):
        """ Test for the presence of docstrings in Client class """
        self.assertIsNot(Client.__doc__, None,
                         "No documentation found for Client class")
        self.assertTrue(len(Client.__doc__) >= 1,
                        "No documentation found for Client class")

    def test_client_func_docstrings(self):
        """ Test for the presence of docstrings in Client methods """
        for func in self.client_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestClient(unittest.TestCase):
    """ Test the Client class """
    info = {"first_name": "radouane",
            "last_name": "abounouas",
            "email": "radouane@tmail.com",
            "password": "red1234"}

    def test_is_subclass(self):
        """ Test the subclass of Client """
        client_1 = Client(**self.info)
        self.assertIsInstance(client_1, Person)
        self.assertIsInstance(client_1, BaseModel)
        self.assertTrue(hasattr(client_1, "id"))
        self.assertTrue(hasattr(client_1, "created_at"))
        self.assertTrue(hasattr(client_1, "updated_at"))
        self.assertTrue(hasattr(client_1, "first_name"))
        self.assertTrue(hasattr(client_1, "last_name"))
        self.assertTrue(hasattr(client_1, "email"))
        self.assertTrue(hasattr(client_1, "password"))

    def test_attributes(self):
        """ Test the attributes of the Client class """
        client_2 = Client(**self.info)
        client_dict = client_2.to_dict()
        self.assertEqual(type(client_dict), dict)
        self.assertFalse("_sa_instance_state" in client_dict)
        for attr in client_2.__dict__:
            if attr not in ["_sa_instance_state", "password"]:
                self.assertTrue(attr in client_dict,
                                f"{attr} not in Owner.to_dict()")
        self.assertTrue("__class__" in client_dict)
        self.assertEqual(client_2.first_name, self.info["first_name"])
        self.assertEqual(client_2.last_name, self.info["last_name"])
        self.assertEqual(client_2.email, self.info["email"])
        self.assertEqual(client_2.password,
                         md5(self.info["password"].encode()).hexdigest())

    def test_to_dict(self):
        """ Test the to_dict method """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        test_client = Client(**self.info)
        test_dict = test_client.to_dict()
        self.assertEqual(test_dict["__class__"], "Client")
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)
        self.assertEqual(test_dict["created_at"],
                         test_client.created_at.strftime(time_format))
        self.assertEqual(test_dict["updated_at"],
                         test_client.updated_at.strftime(time_format))

    def test_client__str__(self):
        """ Test the __str__ method """
        name = "test client"
        test_client = Client(**self.info)

        test_string = "[Client] ({}) {}".format(
            test_client.id, test_client.__dict__)
        self.assertEqual(test_string, str(test_client))
