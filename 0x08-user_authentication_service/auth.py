#!/usr/bin/env python3
""" Password auth module """
import bcrypt
from db import DB
from user import User
import uuid
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Hash the password """
    password = password.encode('UTF-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    return password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initialize auth class """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a user """
        try:
            check_user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            password = _hash_password(password)
            new_user = self._db.add_user(email, password)
            return User

    def valid_login(self, email: str, password: str) -> bool:
        """ Check if an email matches a password """
        try:
            login_user = self._db.find_user_by(email=email)
            password = password.encode('utf-8')
            if bcrypt.checkpw(password, login_user.hashed_password):
                return True
            return False
        except Exception:
            return False

    def _generate_uuid() -> str:
        """ Create a UUID """
        return str(uuid.uuid4())