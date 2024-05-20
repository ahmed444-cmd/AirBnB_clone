#!/usr/bin/python3
""" Specifies the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Representing an amenity class.
    Attributes:
        name (str) : Amenity name
    """

    name = ""
