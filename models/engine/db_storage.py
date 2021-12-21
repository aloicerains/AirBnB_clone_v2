#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker


class DBStorage:
    """Manages storage to MySQL DB"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor - create sqlachemy engine"""
        # engine creation
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        # check if HBNB_ENV  is equal to test (drop tables)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    def classes(self):
        """Returns a dict of all classes"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        clas =  {'State': State,
                 'City': City,
                 'User': User, 
                 'Place': Place,
                 'Review': Review,
                 'Amenity': Amenity}
        return clas

    def all(self, cls=None):
        """Queries and returns all objects depending on cls"""
        d = {}
        if cls is None:
            # for k, v in self.classes().items():
            #     for row in self.__session.query(v).all():
            #         d.update({'{}.{}'.format(type(row).__name__, 
            #                                  row.id,): row})
            return self.__objects
        else:
            cls = self.classes()[cls]
            for row in self.__session.query(cls).all():
                print(row)
                d.update({'{}.{}'.format(type(cls).name, row.id,): row})
        return d

    def new(self, obj):
        """Adds obj to current db session"""
        self.__session.add(obj)
    
    def save(self):
        """Commits changes of current db session"""
        Base.metadata.create_all(self.__engine)
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current db session"""
        if obj:
            name = self.classes()[type(obj).__name__]
            self.__session.query(name).filter(name.id == obj.id).delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """Close session"""
        self.__session.remove()
