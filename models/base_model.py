#!/usr/bin/python3
"""
This module contains the BaseModel class which defines all common
attributes or methods of other classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class defines all common attributes/methods for other classes

    Attributes:
    >> id: [string] - assign with an uuid when an instance is created
    using uuid.uuid4() to have a unique id for each BaseModel

    >> created_at: [datetime] - assign with the current datetime when an
                   instance is created

    >> updated_at: [datetime] - assign with the current datetime when an
                   instance is created, and it will be updated everytime
                   the object is changed

    Methods:
    >> save(self): updates the public instance attribute update_at with
    the current datetime

    >> to_dict(self): returns a dictionary containing all keys/values of
    __dict__ of the instance
    """
    def __init__(self, *args, **kwargs):
        """
        This initializes the BaseModel class
        """
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        This gives the string representation of the BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        This updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This returns a dictionary containig all keys/values of the
        instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return (new_dict)
