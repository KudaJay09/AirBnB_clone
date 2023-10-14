#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User class.

    Attrib:
        email (str): The email of the user.
        password (str): Password of the user.
        first_name (str): Inital name of user.
        last_name (str): Last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
