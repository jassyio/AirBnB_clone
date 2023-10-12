#!/usr/bin/python3
"""
User creation class

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines attributes for the user creation
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""