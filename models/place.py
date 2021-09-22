#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
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
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def reviews(self):
            """Review relationship with Places on File"""
            list_of_reviews = []
            for key, val in models.storage.items():
                if type(val).__name__ == "Review":
                    if val.place_id == self.id:
                        list_of_reviews.append(val)
            return (list_of_reviews)

        @property
        def amenities(self):
            """returns list of amenity instances"""
            res = []
            for i in models.storage.all(Amenity).values():
                if i.id == self.amenity_ids:
                    res.append(i)
            return res

        @amenities.setter
        def amenities(self, value):
            """setter for amenities"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
            else:
                pass
