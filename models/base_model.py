#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

""" 
 base class module 
"""
class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """
    def __init__(self, *args, **kwargs):
        """
        Public instance artributes initialization
        after creation

        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values
        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
           for key,value in kwargs.items():
            if key == 'created_at':
                self.__dict__[key]=datetime.strptime(value, DATE_TIME_FORMAT)
            elif key == 'updated_at':
                self.__dict__[key]=datetime.strptime(value, DATE_TIME_FORMAT)
            elif key == 'id':
                self.__dict__[key]= str(value)
            else:
                self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        temp_dict={}
        for key,value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                temp_dict[key] = value.isoformat()
            else:
                temp_dict[key] = value 
        temp_dict["__class__"] = self.__class__.__name__ 
        return temp_dict