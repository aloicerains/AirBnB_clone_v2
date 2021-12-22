#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade='all, delete-orphan',
                           backref='place')
    amenities = relationship("Amenity", secondary='place_amenity',
                             backref='place_amenities', viewonly=False)

    @property
    def reviews(self):
        """Returns reviews with similar place_id"""
        dic_t = models.storage.all(models.Review)
        reviews = []
        for review in dic_t.values():
            if review.place_id == self.id:
                reviews.append(review)
            return reviews

    @property
    def amenities(self):
        """Returns instances of amenities"""
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        dic_t = storage.all('Amenity')
        amenities = []
        for amenity in dic_t.values():
            if amenity.id in amenity_ids:
                amenities.append(amenity)
        return amenities

    @amenities.setter
    def amenities(self, obj):
        """sets amenities_id attribute"""
        if instance(obj, Amenity):
            if self.id == obj.place_id:
                self.amenity_ids.append(obj.id)
