#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test class for base Model
    """
    def setUp(self):
        """
        fuction for setting up classes needed in testing
        """
        pass

    def test_basic(self):
        """
        testing basic functionalities for base model
        """
        myclass = BaseModel()
        myclass.name="My class"
        myclass.my_number= 100
        self.assertEqual([myclass.name,myclass.my_number],["My class",100])

    def test_Json(self):
        """ test the json repr"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual([my_new_model.id, my_new_model.name, my_new_model.created_at, my_new_model.my_number],
                        [my_model.id, my_model.name, my_model.created_at, my_model.my_number])
                        
if __name__ == "__main__":
    unittest.main()


