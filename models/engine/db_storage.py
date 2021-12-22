#!/usr/bin/python3
"""DBStorage module"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os

classes = {'User': User, 'State': State, 'Place': Place, 'City': City,
           'Amenity': Amenity, 'Review': Review}


class DBStorage:
    """The database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """initializations"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries the current database session based on class name"""
        dictionary = {}
        if cls:
            for obj in classes:
                if cls == obj:
                    result = self.__session.query(classes[obj]).all()
                    for r in result:
                        key = r.__class__.__name__ + "." + r.id
                        dictionary[key] = r
        elif (cls is None):
            for obj in classes:
                result = self.__session.query(classes[obj]).all()
                for r in result:
                    key = r.__class__.__name__ + "." + r.id
                    dictionary[key] = r
        return dictionary

    def new(self, obj):
        """Adds object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from current database session obj"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self, remove=False):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        if remove:
            Session.remove()
        self.__session = Session()

    def close(self):
        """Terminates"""
        self.reload(remove=True)
