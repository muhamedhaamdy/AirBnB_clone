#!/usr/bin/python3
"""Create a unique FileStorage instance"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.user import User

classes_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
storage = FileStorage()
storage.reload()
