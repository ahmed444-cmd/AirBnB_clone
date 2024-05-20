#!/usr/bin/python3
"""
Specifies the FileStorage class.
Authors: Ahmed ELABID
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes & deserializes instances to a JSON file &
     JSON file to instances."""
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "Amenity": Amenity, "City": City, "Review": Review,
               "State": State}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Assigns the object with the key <object class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes the __objects dictionary to the JSON file."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                if cls_name in FileStorage.classes:
                    cls = FileStorage.classes[cls_name]
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
