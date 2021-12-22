#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ''

        @property
        def cities(self):
            """method to find cities"""
            lis_t = []
            for city in storage.all(City).values():
                if getattr(city, "state_id") == self.id:
                    lis_t.append(city)
            return(lis_t)
