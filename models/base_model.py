#!/usr/bin/python3
"""
Specifies the BaseModel class.
Authors: Ahmed ELABID
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """Defines the base model."""

    def __init__(self, *args, **kwargs):
        """Creates a new instance of the BaseModel class."""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Provides the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Updates the 'updated_at' attribute of the instance with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary comprising all keys and values of the instance."""
        result = dict(self.__dict__)
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result
