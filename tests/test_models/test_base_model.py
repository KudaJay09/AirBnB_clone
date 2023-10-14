"""
This module contains the various test for the BaseModel to ascertain
the functionality of the model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    This Class contains the test suites for the BaseModel class
    """

    def setUp(self):
        """
        Setup the BaseModel for testing
        """
        self.base_model = BaseModel()

    def test_uuid_is_present(self):
        """
        Checking if uuid was added
        """
        self.assertTrue(self.base_model.id is not None)

    def test_uuid_not_same_for_other_instances(self):
        """
        Checking if uuid is not the same for another instance
        """
        base_model_2 = BaseModel()
        self.assertNotEqual(self.base_model.id, base_model_2.id)

    def test_created_at_is_present(self):
        """
        Checking if created_at was added
        """
        self.assertTrue(self.base_model.created_at is not None)

    def test_created_at_not_same_for_other_instances(self):
        """
        Checking if created_at is not the same for another instance
        """
        base_model_2 = BaseModel()
        self.assertNotEqual(self.base_model.created_at,
                            base_model_2.created_at)

    def test_updated_at_is_present(self):
        """
        Checking if updated_at was added
        """
        self.assertTrue(self.base_model.updated_at is not None)

    def test_updated_at_not_same_for_other_instances(self):
        """
        Checking if updated_at is not the same for another instance
        """
        base_model_2 = BaseModel()
        self.assertNotEqual(self.base_model.updated_at,
                            base_model_2.updated_at)

    def test_string_rep_returns_expected_format(self):
        """
        Checking that the __str__ method is working as customed
        """
        expected_id = self.base_model.id
        expected_dict = self.base_model.__dict__
        expected_output = "[BaseModel] ({}) {}".format(expected_id,
                                                       expected_dict)
        self.assertEqual(self.base_model.__str__(), expected_output)

    def test_to_dict_has_all_keys_values_of_dict_of_instance(self):
        """
        Checking all keys/values of the __dict__ of the instance is present
        """
        self.base_model.name = 'My First Model'
        self.base_model.my_number = 89
        base_id = self.base_model.id
        base_created_at = self.base_model.created_at.isoformat()
        base_updated_at = self.base_model.updated_at.isoformat()
        expected_output = {'id': base_id,
                           'created_at': base_created_at,
                           'updated_at': base_updated_at,
                           'name': 'My First Model', 'my_number': 89,
                           '__class__': 'BaseModel'}
        self.assertEqual(self.base_model.to_dict(), expected_output)

    def test_base_model_with_kwargs_parameter(self):
        """
        Checking if BaseModel works with kwargs parameter
        """
        base_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_dict)
        self.assertTrue(new_base_model.id)
        self.assertTrue(new_base_model.created_at)
        self.assertTrue(new_base_model.updated_at)

    def test_base_model_created_at_and_updated_at_is_datetime_object(self):
        """
        Checking if BaseModel works with kwargs parameter,and
        created_at and updated_at is datetime object
        """
        base_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_dict)
        self.assertTrue(type(new_base_model.created_at) is datetime)
        self.assertTrue(type(new_base_model.updated_at) is datetime)

    def test_base_model_with_kwargs_parameter_are_diff_obj(self):
        """
        Checking if BaseModel works with kwargs parameter,
        and the two objects are not the same
        """
        base_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_dict)
        self.assertTrue(new_base_model is not self.base_model)

    def test_save_updates_the_expected_fields(self):
        """
        Checking updates updated_at with current datetime
        """
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)
