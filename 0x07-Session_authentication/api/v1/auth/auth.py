#!/usr/bin/env python3
""" Authorization class """
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ Authorization class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require Authentication """
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        path2 = list(path)
        if path2[0] == '/':
            del path2[0]
        if path2[-1] == '/':
            del path2[-1]
        path = "".join(path2)
        for i in range(len(excluded_paths)):
            temp = list(excluded_paths[i])
            if temp[0] == '/':
                del temp[0]
            if temp[-1] == '/':
                del temp[-1]
            excluded_paths[i] = "".join(temp)
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Check if header has key """
        if request is None:
            return None
        keys = request.headers
        if keys.get('Authorization') is None:
            return None
        return keys.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None

    def session_cookie(self, request=None):
        """ Get the session cookie """
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
