#!/usr/bin/python3
""" State Module for HBNB project """
import models  # noqa
from models.base_model import BaseModel
# from models.place import place_amenity
# from os import getenv
from sqlalchemy import Table, Column, String, ForeignKey  # noqa
from sqlalchemy.orm import relationship  # noqa


class Amenity(BaseModel):
    """MySQL database for Amanity.
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    # if getenv('HBNB_TYPE_STORAGE') == 'db':
    #     __tablename__ = 'amenities'
    #     name = Column(String(128),
    #                   nullable=False)
    #     place_amenities = relationship(
    #         'Place',
    #         secondary=place_amenity, back_populates='amenities'
    #     )
    # else:
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
