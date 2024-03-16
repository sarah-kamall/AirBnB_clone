#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.place import Place
from datetime import datetime
import time

class TestPlace(unittest.TestCase):
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
        myPlace = Place()
        self.assertEqual(type(myPlace.city_id),str)
        self.assertEqual(type(myPlace.user_id),str)
        self.assertEqual(type(myPlace.name),str)
        self.assertEqual(type(myPlace.description),str)
        self.assertEqual(type(myPlace.number_rooms),int)
        self.assertEqual(type(myPlace.number_bathrooms),int)
        self.assertEqual(type(myPlace.max_guest),int)
        self.assertEqual(type(myPlace.price_by_night),int)
        self.assertEqual(type(myPlace.latitude),float)
        self.assertEqual(type(myPlace.longitude),float)
        self.assertEqual(type(myPlace.amenity_ids),list)


    
if __name__ == "__main__":
    unittest.main()


