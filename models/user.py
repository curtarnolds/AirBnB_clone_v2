#!/usr/bin/python3
"""This module defines a class User"""
import hashlib  # noqa
import models  # noqa
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """MySQL database user. Inherits from SQLAlchemy Base and links to the
    MySQL table users.
      Attributes:
      __tablename__ (str): The name of the MySQL table to store users.
      email: (sqlalchemy String): The user's email address.
      password (sqlalchemy String): The user's password.
      first_name (sqlalchemy String): The user's first name.
      last_name (sqlalchemy String): The user's last name.
      places (sqlalchemy relationship): The User-Place relationship.
      reviews (sqlalchemy relationship): The User-Review relationship.
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128),
                       nullable=False)
        password = Column('password',
                          String(128),
                          nullable=False)
        first_name = Column(String(128),
                            nullable=True)
        last_name = Column(String(128),
                           nullable=True)
        places = relationship("Place",
                              back_populates="user",
                              cascade="all, delete")
        reviews = relationship("Review",
                               back_populates="user",
                               cascade="all, delete")
    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    # @property
    # def password(self):
    #     return self._password

    # @password.setter
    # def password(self, pwd):
    #     """hashing password values"""
    #     self._password = pwd
