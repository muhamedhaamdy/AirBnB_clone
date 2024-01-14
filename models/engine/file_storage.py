#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
    
    def save(self):
        with open(self.__file_path, 'w') as f:
            serialized_objects = {k: v.to_dict() for k, v in self.__objects.items()}
            f.write(json.dumps(serialized_objects))

    def reload(self):
        """
        Loads the storage dictionary from a JSON file.
        """
        try:
            with open(self.__file_path, "r") as f:
                objdicts = json.load(f)
                for val in objdicts.values():
                    self.new(eval(val["__class__"])(**val))
        except FileNotFoundError:
            pass
