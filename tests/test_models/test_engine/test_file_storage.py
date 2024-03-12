#!/usr/bin/python3
"""
Test suits for the base model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    Test class for File Storage
    """
    def setUp(self):
        """
        fuction for setting up classes needed in testing
        """
        pass

    def test_file_path(self):
        """
        test if a valid file path
        """
        fs = FileStorage()
        self.assertNotEqual(fs.get_file_path(), None)
    
    def test_file_path(self):
        """
        test if a valid objects
        """
        fs = FileStorage()
        self.assertEqual(type(fs.__objects),dict)

if __name__ == "__main__":
    unittest.main()


