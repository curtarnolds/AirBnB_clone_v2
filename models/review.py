#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship  # noqa


class Review(BaseModel):
    """ Review classto store review information
    Attributes:
        __tablename__ (str): The name of the MySQL table to store Reviews.
        text (sqlalchemy String): The review description.
        place_id (sqlalchemy String): The review's place id.
        user_id (sqlalchemy String): The review's user id.
    """
    # if getenv('HBNB_TYPE_STORAGE') == 'db':
    #     __tablename__ = 'reviews'
    #     text = Column(String(1024),
    #                   nullable=False)
    #     place_id = Column(String(60),
    #                       ForeignKey('places.id'),
    #                       nullable=False)
    #     user_id = Column(String(60),
    #                      ForeignKey('users.id'),
    #                      nullable=False)
    #     user = relationship('User', back_populates='reviews')
    # else:
    text = ""
    place_id = ""
    user_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
