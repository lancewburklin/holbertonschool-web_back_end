#!/usr/bin/env python3
""" Session Authentication """
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Session Auth class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a session ID """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        sess = str(uuid.uuid4())
        self.user_id_by_session_id[sess] = user_id
        return sess

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Get session ID """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Overload the current user """
        if request is None:
            return None
        cook = self.session_cookie(request)
        if cook is None:
            return None
        the_id = self.user_id_by_session_id.get(cook)
        if the_id is None:
            return None
        return User.get(the_id)
