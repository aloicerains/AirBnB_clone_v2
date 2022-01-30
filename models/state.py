#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """ State class """

    # if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
    # else:
    #    name = ''
    # def __init__(self, *args, **kwargs):
    #   """State init"""
    #   super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """method to return city objects"""
            lis_t = []
            for city in models.storage.all(City).values():
                if getattr(city, "state_id") == self.id:
                    lis_t.append(city)
            return(lis_t)
