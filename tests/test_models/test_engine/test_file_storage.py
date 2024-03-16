#!/usr/bin/python3
"""
Test suits for the base model
"""
import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage
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
    
    def test_objects_type(self):
        """
        test if a valid objects
        """
        fs = FileStorage()
        objs = fs.all()
        self.assertEqual(type(objs),dict)

    def test_save(self):
        """
        test save function
        """
        my_model=BaseModel()
        my_model.save()
        fs = FileStorage()
        found =0 
        
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            
            if ((my_model.__class__.__name__ +'.' + my_model.id) == obj_id):
                found += 1
        self.assertEqual(found, 1)

        
    def test_reload(self):
        """
        test reload function
        """
        bm = BaseModel()
        fs = FileStorage()
        bm.updated_at = datetime.utcnow()
        bm.name= "test"
        fs.new(bm)
        
        try:    
            os.remove(fs.get_file_path())
        except:

            pass
        fs.save()
        try:
            fs._FileStorage__objects.clear()
        except:
            pass
        fs.reload()

        all_reloaded = fs.all()
        found =1
        print(bm.id)
        if all_reloaded.get(bm.id) is None and all_reloaded.get("{}.{}".format("BaseModel", bm.id)) is None:
            found =0
        self.assertNotEqual(found, 0)
if __name__ == "__main__":
    unittest.main()


