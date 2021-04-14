#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy import update
from user import User

from user import Base


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add a user to the Database """
        newUser = User()
        newUser.email = email
        newUser.hashed_password = hashed_password
        self._session.add(newUser)
        self._session.commit()
        return newUser

    def find_user_by(self, **kwargs) -> User:
        """ Find a user based of attribute """
        users = self._session.query(User).filter_by(**kwargs).all()
        if len(users) == 0:
            raise NoResultFound
        else:
            return users[0]
        raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update the user """
        per = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if not hasattr(per, k):
                raise ValueError
            setattr(per, k, v)
        self._session.commit()
        return None
