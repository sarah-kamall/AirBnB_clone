#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.state import State
from datetime import datetime
import time

class TestState(unittest.TestCase):
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
        myState = State()
        self.assertEqual(type(myState.name),str)
  
if __name__ == "__main__":
    unittest.main()


