#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import ForeignKey, String,Column
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name 
     Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128),
                      nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id'),
                          nullable=False)
        places = relationship("Place",
                              backref="cities",
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
