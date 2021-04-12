#!/usr/bin/env python3
""" Creating the Database """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from user import Base


class DB:

    def __init__(self):
        """ Initialize the class """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str):
        """ Add a user to the Database """
        from user import User
        newUser = User()
        newUser.email = email
        newUser.hashed_password = hashed_password
        self._session.add(newUser)
        self._session.commit()
        return newUser
