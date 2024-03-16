#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.user import User
from datetime import datetime
import time

class TestUser(unittest.TestCase):
    """
    Test class for base Model
    """
    def setUp(self):
        """
        fuction for ;2setting up classes needed in testing
        """
        pass

    def test_basic_user(self):
        """
        testing basic functionalities for base model
        """
        myclass = User()
        myclass.email="Myuser@mail"
        myclass.password= "123"
        myclass.first_name= "name"
        myclass.last_name = "lname"
        self.assertEqual([myclass.email,myclass.password,myclass.first_name, myclass.last_name],["Myuser@mail","123","name","lname"])

    def test_Json(self):
        """ test the json repr"""
        myclass = User()
        myclass.email="Myuser@mail"
        myclass.password= "123"
        myclass.first_name= "name"
        myclass.last_name = "lname"
        myclassjson= myclass.to_dict()
        my_new_model = User(**myclassjson)
        self.assertEqual([myclass.email,myclass.password,myclass.first_name, myclass.last_name],
                        [my_new_model.email,my_new_model.password,my_new_model.first_name, my_new_model.last_name])

   

if __name__ == "__main__":
    unittest.main()


