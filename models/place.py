#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base, BaseModel
from models.review import Review  # noqa
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table  # noqa
from sqlalchemy.orm import relationship


# place_amenity = Table('place_amenity',
#                       Base.metadata,
#                       Column('place_id', String(60), ForeignKey('places.id'),
#                              primary_key=True),
#                       Column('amenity_id', String(60),
#                              ForeignKey('amenities.id'),
#                              primary_key=True))


class Place(BaseModel, Base):
    """Representation of Place
     Attributes:
        __tablename__ (str): The name of the MySQL table to store places.
        city_id (sqlalchemy String): The place's city id.
        user_id (sqlalchemy String): The place's user id.
        name (sqlalchemy String): The name.
        description (sqlalchemy String): The description.
        number_rooms (sqlalchemy Integer): The number of rooms.
        number_bathrooms (sqlalchemy Integer): The number of bathrooms.
        max_guest (sqlalchemy Integer): The maximum number of guests.
        price_by_night (sqlalchemy Integer): The price by night.
        latitude (sqlalchemy Float): The place's latitude.
        longitude (sqlalchemy Float): The place's longitude.
        reviews (sqlalchemy relationship): The Place-Review relationship.
        amenities (sqlalchemy relationship): The Place-Amenity relationship.
        amenity_ids (list): An id list of all linked amenities.
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60),
                         ForeignKey("cities.id"),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
        name = Column(String(128),
                      nullable=False)
        description = Column(String(1024),
                             nullable=True)
        number_rooms = Column(Integer,
                              default=0,
                              nullable=False)
        number_bathrooms = Column(Integer,
                                  default=0,
                                  nullable=False)
        max_guest = Column(Integer,
                           default=0,
                           nullable=False)
        price_by_night = Column(Integer,
                                default=0,
                                nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        # reviews = relationship("Review", cascade="all, delete",
        #                        backref="places")
        # amenities = relationship("Amenity",
        #                          secondary='place_amenity',
        #                          viewonly=False,
        #                          backref="place_amenities")
        cities = relationship('City', back_populates='places')
        user = relationship('User', back_populates='places')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """attribute that returns list of Review instances"""
        values_review = models.storage.all("Review").values()
        list_review = []
        for review in values_review:
            if review.place_id == self.id:
                list_review.append(review)
        return list_review

    # if getenv('HBNB_TYPE_STORAGE') != 'db':
    #     @property
    #     def amenities(self):
    #         """attribute that returns list of Amenity instances"""
    #         values_amenity = models.storage.all("Amenity").values()
    #         list_amenity = []
    #         for amenity in values_amenity:
    #             if amenity.place_id == self.id:
    #                 list_amenity.append(amenity)
    #         return list_amenity

    #     @amenities.setter
    #     def amenities(self, amenity):
    #         """Add Amenity.id to amenity_ids"""
    #         from models.amenity import Amenity  # noqa
    #         if isinstance(amenity, Amenity):
    #             self.amenity_ids.append(amenity.id)
    #         else:
    #             pass
