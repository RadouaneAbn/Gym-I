#!/usr/bin/python3
from server.models.owner import Owner
from server.models.base_model import BaseModel
from server.models.person import Person
from server.models import owner
from hashlib import md5
import unittest
import inspect
import pep8


class Owner_check(unittest.TestCase):
    """ Test pycodestyle and documentation of the modules """
    @classmethod
    def setUpClass(cls):
        """ Set up a list of tuples("class_name", class_obj) """
        cls.owner_f = inspect.getmembers(Owner, inspect.isfunction)

    def test_pep8_owner(self):
        """ Test the pycodestyle of owner.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['server/models/owner.py'])
        self.assertEqual(result.total_errors, 0,
                         "** owner.py: PyCodeStyle Failed !!!")

    def test_pep8_test_owner(self):
        """ Test the pycodestyle of test_owner.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_owner.py'])
        self.assertEqual(result.total_errors, 0,
                         "** test_owner.py: PyCodeStyle Failed !!!")

    def test_owner_module_docstring(self):
        """ Test for the presence of docstrings in owner model """
        self.assertIsNot(owner.__doc__, None,
                         "No documentation found for owner module")
        self.assertTrue(len(owner.__doc__) >= 1,
                        "No documentation found for owner module")

    def test_owner_class_docstring(self):
        """ Test for the presence of docstrings in Owner class """
        self.assertIsNot(Owner.__doc__, None,
                         "No documentation found for Owner class")
        self.assertTrue(len(Owner.__doc__) >= 1,
                        "No documentation found for Owner class")

    def test_owner_func_docstrings(self):
        """ Test for the presence of docstrings in Owner methods """
        for func in self.owner_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestOwner(unittest.TestCase):
    """ Test the Owner class """
    info = {"first_name": "radouane",
            "last_name": "abounouas",
            "email": "radouane@tmail.com",
            "password": "red1234"}

    def test_is_subclass(self):
        """ Test the subclass of Owner """
        owner_1 = Owner(**self.info)
        self.assertIsInstance(owner_1, Person)
        self.assertIsInstance(owner_1, BaseModel)
        self.assertTrue(hasattr(owner_1, "id"))
        self.assertTrue(hasattr(owner_1, "created_at"))
        self.assertTrue(hasattr(owner_1, "updated_at"))
        self.assertTrue(hasattr(owner_1, "first_name"))
        self.assertTrue(hasattr(owner_1, "last_name"))
        self.assertTrue(hasattr(owner_1, "email"))
        self.assertTrue(hasattr(owner_1, "password"))

    def test_attributes(self):
        """ Test the attributes of the Owner class """
        owner_2 = Owner(**self.info)
        owner_dict = owner_2.to_dict()
        self.assertEqual(type(owner_dict), dict)
        self.assertFalse("_sa_instance_state" in owner_dict)
        for attr in owner_2.__dict__:
            if attr not in ["_sa_instance_state", "password"]:
                self.assertTrue(attr in owner_dict,
                                f"{attr} not in Owner.to_dict()")
        self.assertTrue("__class__" in owner_dict)
        self.assertEqual(owner_2.first_name, self.info["first_name"])
        self.assertEqual(owner_2.last_name, self.info["last_name"])
        self.assertEqual(owner_2.email, self.info["email"])
        self.assertEqual(owner_2.password,
                         md5(self.info["password"].encode()).hexdigest())

    def test_to_dict(self):
        """ Test the to_dict method """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        test_owner = Owner(**self.info)
        test_dict = test_owner.to_dict()
        self.assertEqual(test_dict["__class__"], "Owner")
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)
        self.assertEqual(test_dict["created_at"],
                         test_owner.created_at.strftime(time_format))
        self.assertEqual(test_dict["updated_at"],
                         test_owner.updated_at.strftime(time_format))

    def test_owner__str__(self):
        """ Test the __str__ method """
        name = "test owner"
        test_owner = Owner(**self.info)

        test_string = "[Owner] ({}) {}".format(
            test_owner.id, test_owner.__dict__)
        self.assertEqual(test_string, str(test_owner))
