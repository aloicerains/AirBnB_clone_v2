#!/usr/bin/python3
"""Adds a conditional depending of the value of the environment var for
switching btwn storage types"""
from os import environ
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review

# determine storage from env
if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    # filestorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
