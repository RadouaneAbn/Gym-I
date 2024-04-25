#!/usr/bin/python3

from server.models.base_model import BaseModel
from server.models import base_model
import unittest
import inspect
import pep8


class BaseModel_check(unittest.TestCase):
    """ Test pycodestyle and documentation of teh modules """
    @classmethod
    def setUpClass(cls):
        """ Set up a list of tuples("class_name", class_obj) """
        cls.basemodel_f = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_basemodel(self):
        """ Test the pycodestyle of base_model.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['server/models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "** base_model.py: PyCodeStyle Failed !!!")

    def test_pep8_test_basemodel(self):
        """ Test the pycodestyle of test_base_model.py """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "** test_base_model.py: PyCodeStyle Failed !!!")

    def test_basemodel_module_docstring(self):
        """  """
        self.assertIsNot(base_model.__doc__, None,
                         "No documentation found for basemodel module")
        self.assertTrue(len(base_model.__doc__) >= 1,
                        "No documentation found for basemodel module")

    def test_basemodel_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "No documentation found for BaseModel class")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "No documentation found for BaseModel class")

    def test_basemodel_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.basemodel_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBaseModel(unittest.TestCase):
    """ Test the BaseModel class """
    def test_is_subclass(self):
        """ Test the subclass of basemodel """
        basemodel_1 = BaseModel()
        self.assertIsInstance(basemodel_1, BaseModel)
        self.assertTrue(hasattr(basemodel_1, "id"))
        self.assertTrue(hasattr(basemodel_1, "created_at"))
        self.assertTrue(hasattr(basemodel_1, "updated_at"))

    def test_attributes(self):
        """ Test the attributes of the BaseModel class """
        test_name = "basemodel test"
        basemodel_2 = BaseModel(name=test_name)
        basemodel_dict = basemodel_2.to_dict()
        self.assertEqual(type(basemodel_dict), dict)
        self.assertFalse("_sa_instance_state" in basemodel_dict)
        for attr in basemodel_2.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in basemodel_dict)
        self.assertTrue("__class__" in basemodel_dict)

    def test_to_dict(self):
        """ Test the to_dict method """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        name = "test basemodel"
        test_basemodel = BaseModel(name=name)
        test_dict = test_basemodel.to_dict()
        self.assertEqual(test_dict["__class__"], "BaseModel")
        self.assertEqual(type(test_dict["created_at"]), str)
        self.assertEqual(type(test_dict["updated_at"]), str)
        self.assertEqual(test_dict["created_at"],
                         test_basemodel.created_at.strftime(time_format))
        self.assertEqual(test_dict["updated_at"],
                         test_basemodel.updated_at.strftime(time_format))

    def test_basemodel__str__(self):
        """ Test the __str__ method """
        test_basemodel = BaseModel()

        test_string = "[BaseModel] ({}) {}".format(
            test_basemodel.id, test_basemodel.__dict__)
        self.assertEqual(test_string, str(test_basemodel))
