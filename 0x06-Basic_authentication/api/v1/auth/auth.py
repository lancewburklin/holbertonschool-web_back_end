#!/usr/bin/env python3
""" Authorization class """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authorization class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require Authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization Header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None
