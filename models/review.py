#!/usr/bin/python3
"""Defines the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review
    
    Attrib:
        place_id (str): The Place id.
        user_id (str): The User.id
        text (str): 
    """

    place_id = ""
    user_id = ""
    text = ""