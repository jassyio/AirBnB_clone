#!/usr/bin/python3
"""
Defines a city

"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines a city to look for"""
    state_id = ""
    name = ""