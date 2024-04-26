#!/usr/bin/python3
from server.models.amenity import Amenity
from server.models.base_model import BaseModel
from server.models import amenity
import unittest
import inspect
import pep8


class Amenity_check(unittest.TestCase):
    """ Test pycodestyle and documentation of teh modules """
    @classmethod
    def setUpClass(cls):
        """ Set up a list of tuples("class_name", class_obj) """
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_amenity(self):
        """ Test the pycodestyle of amenity.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['server/models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "** amenity.py: PyCodeStyle Failed !!!")

    def test_pep8_test_amenity(self):
        """ Test the pycodestyle of test_amenity """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "** test_amenity.py: PyCodeStyle Failed !!!")

    def test_amenity_module_docstring(self):
        """ Test for the presence of docstrings in city model """
        self.assertIsNot(amenity.__doc__, None,
                         "No documentation found for amenity module")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "No documentation found for amenity module")

    def test_amenity_class_docstring(self):
        """ Test for the presence of docstrings in City class """
        self.assertIsNot(Amenity.__doc__, None,
                         "No documentation found for Amenity class")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "No documentation found for Amenity class")

    def test_amenity_func_docstrings(self):
        """ Test for the presence of docstrings in Amenity methods """
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """ Test the Amenity class """
    def test_is_subclass(self):
        """ Test the subclass of Amenity """
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1, BaseModel)
        self.assertTrue(hasattr(amenity_1, "id"))
        self.assertTrue(hasattr(amenity_1, "created_at"))
        self.assertTrue(hasattr(amenity_1, "updated_at"))

    def test_attributes(self):
        """ Test the attributes of the Amenity class """
        test_name = "amenity test"
        amenity_2 = Amenity(name=test_name)
        amenity_dict = amenity_2.to_dict()
        self.assertEqual(type(amenity_dict), dict)
        self.assertFalse("_sa_instance_state" in amenity_dict)
        for attr in amenity_2.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in amenity_dict)
        self.assertTrue("__class__" in amenity_dict)
        self.assertTrue("name" in amenity_2.__dict__,
                        "name attribute is not in the amenity")
        self.assertTrue("name" in amenity_2.to_dict(),
                        "name attribute is not in the amenity")
        self.assertEqual(amenity_2.name, test_name)

    def test_to_dict(self):
        """ Test the to_dict method """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        name = "test amenity"
        test_amenity = Amenity(name=name)
        test_dict = test_amenity.to_dict()
        self.assertEqual(test_dict["__class__"], "Amenity")
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)
        self.assertEqual(test_dict["created_at"],
                         test_amenity.created_at.strftime(time_format))
        self.assertEqual(test_dict["updated_at"],
                         test_amenity.updated_at.strftime(time_format))

    def test_amenity__str__(self):
        """ Test the __str__ method """
        name = "test amenity"
        test_amenity = Amenity(name=name)

        test_string = "[Amenity] ({}) {}".format(
            test_amenity.id, test_amenity.__dict__)
        self.assertEqual(test_string, str(test_amenity))
