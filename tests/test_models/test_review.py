#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.review import Review
from datetime import datetime
import time

class TestReview(unittest.TestCase):
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
        myReview = Review()
        self.assertEqual(type(myReview.place_id),str)
        self.assertEqual(type(myReview.user_id),str)
        self.assertEqual(type(myReview.text),str)
    
if __name__ == "__main__":
    unittest.main()


