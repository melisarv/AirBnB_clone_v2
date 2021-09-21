#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if models.is_db == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade="all")
    else:
        state_id = ""
        name = ""
