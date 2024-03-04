"""#!/usr/bin/python3"""
from uuid import uuid4
from datetime import datetime
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
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """
         updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at=datetime.utcnow()
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        temp_dict=self.__dict__
        temp_dict[__class__]=self.__class__.__name__
        temp_dict['created_at'] = datetime.isoformat(temp_dict['created_at'])
        temp_dict['updated_at'] = datetime.isoformat(temp_dict['updated_at'])
        return temp_dict