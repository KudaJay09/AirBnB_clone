#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
import.models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User


class FileStorage:
    """Represents a storage engine(abstracted)

    Attributes:
        __file_path (str): Name of the file to save objects.
    
        __objects (dict): A dictionary of an abstruct objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets __objects the obj with key <obj class name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

        def save(self):
            """Serializes __objects to the JSON file __file_path"""
            