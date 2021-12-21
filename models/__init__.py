#!/usr/bin/python3
"""Adds a conditional depending of the value of the environment var for
switching btwn storage types"""
from os import environ


# determine storage from env
if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    # filestorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
