#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.amenity import Amenity
from datetime import datetime
import time

class TestAmenity(unittest.TestCase):
    """
    Test class for base Model
    """
    def setUp(self):
        """
        fuction for ;2setting up classes needed in testing
        """
        pass

    
    def testname(self):
        """
        test last_name 
        """
        myAmenity = Amenity()
        self.assertEqual(type(myAmenity.name),str)
  
if __name__ == "__main__":
    unittest.main()


