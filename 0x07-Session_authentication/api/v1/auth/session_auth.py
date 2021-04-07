#!/usr/bin/env python3
""" Session Authentication """
from .auth import Auth
import uuid


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
