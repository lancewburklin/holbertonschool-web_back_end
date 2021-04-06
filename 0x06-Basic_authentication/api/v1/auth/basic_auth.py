#!/usr/bin/env python3
""" Authorizing users """
from .auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """ Basic Auth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract the base64 """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if "Basic " in authorization_header:
            return authorization_header.replace("Basic ", "")
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decode base64 """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base = base64_authorization_header
            base = base64.b64decode(base64_authorization_header)
            return base.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Get credentials """
        de = decoded_base64_authorization_header
        creds = (None, None)
        if de is None:
            return creds
        if type(de) is not str:
            return creds
        if ':' not in de:
            return creds
        parts = de.split(":")
        if parts is None:
            return creds
        creds2 = (parts[0], parts[1])
        return creds2

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Check for user """
        if user_email is None:
            return None
        if user_pwd is None:
            return None
        if type(user_pwd) is not str:
            return None
        if type(user_email) is not str:
            return None
        if User.count == 0:
            return None
        person = User.search({'email': user_email})
        if person is True or person is False or len(person) == 0:
            return None
        for per in person:
            if per.is_valid_password(user_pwd):
                return per
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Define the current user """
        creds = self.authorization_header(request)
        creds = self.extract_base64_authorization_header(creds)
        creds = self.decode_base64_authorization_header(creds)
        creds = self.extract_user_credentials(creds)
        player = self.user_object_from_credentials(creds[0], creds[1])
        return player
