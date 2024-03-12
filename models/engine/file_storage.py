#!/bin/python3
import json
from models.base_model import BaseModel
"""
 JSON file handling
"""
class FileStorage():
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path="file.json"
    __objects = {}
        
    def all(self):
        """
         returns the dictionary __objects
        """
        return self.__objects
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[obj.__class__.__name__ +'.'+ str(obj)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w+') as f:
            json.dump({k:v.to_dict() for k,v in self.__objects.items() },f)
    
    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                dict = json.loads(file.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
    
        