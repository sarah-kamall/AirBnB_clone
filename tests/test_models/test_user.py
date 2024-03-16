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
    def test_name(self):
        """
        test name 
        """
        myUser = User()
        self.assertEqual(type(myUser.first_name),str)
    def test_last_name(self):
        """
        test last_name 
        """
        myUser = User()
        self.assertEqual(type(myUser.last_name),str)
    def test_password(self):
        """
        test password 
        """
        myUser = User()
        self.assertEqual(type(myUser.password),str)
    def test_email(self):
        """
        test email 
        """
        myUser = User()
        self.assertEqual(type(myUser.email),str)
if __name__ == "__main__":
    unittest.main()


