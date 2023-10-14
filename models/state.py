#!/usr/bin/python3
"""Defines the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state
    
    Attrib:
        name (str): Name of the state.
    """
    name = ""