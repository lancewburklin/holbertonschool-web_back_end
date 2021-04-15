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


def _generate_uuid() -> str:
    """ Create a UUID """
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """ Create the session """
        try:
            per = self._db.find_user_by(email=email)
        except Exception:
            return None
        new_id = _generate_uuid()
        self._db.update_user(per.id, session_id=new_id)
        return new_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Get the user from the session ID """
        if session_id is None:
            return None
        try:
            per = self._db.find_user_by(session_id=session_id)
            return per
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ End the session """
        try:
            per = self._db.find_user_by(id=user_id)
            self._db.update_user(per.id, session_id=None)
            return None
        except Exception:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Create a reset token """
        try:
            per = self._db.find_user_by(email=email)
            toke = _generate_uuid()
            self._db.update_user(per.id, reset_token=toke)
            return toke
        except Exception:
            raise ValueError
