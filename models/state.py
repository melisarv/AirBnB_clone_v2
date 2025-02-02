#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all', backref="state")

    if ("HBNB_TYPE_STORAGE", None) is None:
        @property
        def cities(self):
            """returns city list instead"""
            cities_list = []
            all_cities = models.storage.all(City).values()
            for ct in all_cities:
                if ct.state_id == self.id:
                    cities_list.append(ct)
            return cities_list
