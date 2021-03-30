#!/usr/bin/env python3
""" Authorizing users """
from .auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Extract the base64 """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if "Basic " in authorization_header:
            return authorization_header.replace("Basic ", "")
        return None
