#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    if models.is_db == 'db':
        city_id = Column(String(60),
                         ForeignKey('cities.id', ondelete='CASCADE'),
                         nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id', ondelete='CASCADE'),
                         nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place')
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

    if models.is_db != 'db':
        @property
        def reviews(self):
            """Review relationship with Places on File"""
            list_of_reviews = []
            for key, val in models.storage.items():
                if type(val).__name__ == "Review":
                    if val.place_id == self.id:
                        list_of_reviews.append(val)
            return (list_of_reviews)
