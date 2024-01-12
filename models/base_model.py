#!/usr/bin/python3
"""The base object"""
import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """returns the string representation of an object"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values """
        self.updated_at = self.updated_at.isoformat()
        self.created_at = self.created_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
