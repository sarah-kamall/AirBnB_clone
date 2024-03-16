#!/bin/python3
"""
file including City class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """Represent a City

    Attributes:
        state_id (str): represents a name
        name(str): represents a name
    """
    name = ""
    state_id = ""     
    