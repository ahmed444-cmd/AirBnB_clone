#!/usr/bin/python3
"""Definition of the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the Review."""
    place_id = ""
    user_id = ""
    text = ""
