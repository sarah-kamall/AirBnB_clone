#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.city import City
from datetime import datetime
import time

class TestCity(unittest.TestCase):
    """
    Test class for base Model
    """
    def setUp(self):
        """
        fuction for ;2setting up classes needed in testing
        """
        pass

   
    def test_name(self):
        """
        test name 
        """
        myCity = City()
        self.assertEqual(type(myCity.name),str)
        self.assertEqual(type(myCity.state_id),str)
  
if __name__ == "__main__":
    unittest.main()


