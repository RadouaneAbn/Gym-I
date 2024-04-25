#!/usr/bin/python3
from server.models.city import City
from server.models.base_model import BaseModel
from server.models import city
import unittest
import inspect
import pep8


class City_check(unittest.TestCase):
    """ Test pycodestyle and documentation of the modules """
    @classmethod
    def setUpClass(cls):
        """ Set up a list of tuples("class_name", class_obj) """
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_city(self):
        """ Test the pycodestyle of city.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['server/models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "** city.py: PyCodeStyle Failed !!!")

    def test_pep8_test_city(self):
        """ Test the pycodestyle of test_city.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "** test_city.py: PyCodeStyle Failed !!!")

    def test_city_module_docstring(self):
        """ Test for the presence of docstrings in city model """
        self.assertIsNot(city.__doc__, None,
                         "No documentation found for city module")
        self.assertTrue(len(city.__doc__) >= 1,
                        "No documentation found for city module")

    def test_city_class_docstring(self):
        """ Test for the presence of docstrings in City class """
        self.assertIsNot(City.__doc__, None,
                         "No documentation found for City class")
        self.assertTrue(len(City.__doc__) >= 1,
                        "No documentation found for City class")

    def test_city_func_docstrings(self):
        """ Test for the presence of docstrings in City methods """
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """ Test the City class """

    def test_is_subclass(self):
        """ Test the subclass of City """
        city_1 = City()
        self.assertIsInstance(city_1, BaseModel)
        self.assertTrue(hasattr(city_1, "id"))
        self.assertTrue(hasattr(city_1, "created_at"))
        self.assertTrue(hasattr(city_1, "updated_at"))

    def test_attributes(self):
        """ Test the attributes of the City class """
        test_name = "city test"
        city_2 = City(name=test_name)
        city_dict = city_2.to_dict()
        self.assertEqual(type(city_dict), dict)
        self.assertFalse("_sa_instance_state" in city_dict)
        for attr in city_2.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in city_dict)
        self.assertTrue("__class__" in city_dict)
        self.assertTrue("name" in city_2.__dict__,
                        "name attribute is not in the city")
        self.assertTrue("name" in city_2.to_dict(),
                        "name attribute is not in the city")
        self.assertEqual(city_2.name, test_name)

    def test_to_dict(self):
        """ Test the to_dict method """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        name = "test city"
        test_city = City(name=name)
        test_dict = test_city.to_dict()
        self.assertEqual(test_dict["__class__"], "City")
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)
        self.assertEqual(test_dict["created_at"],
                         test_city.created_at.strftime(time_format))
        self.assertEqual(test_dict["updated_at"],
                         test_city.updated_at.strftime(time_format))

    def test_city__str__(self):
        """ Test the __str__ method """
        name = "test city"
        test_city = City(name=name)

        test_string = "[City] ({}) {}".format(
            test_city.id, test_city.__dict__)
        self.assertEqual(test_string, str(test_city))
