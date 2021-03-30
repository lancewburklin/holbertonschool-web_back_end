#!/usr/bin/env python3
""" Authorizing users """
from .auth import Auth
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
            if base64.b64decode(base64_authorization_header):
                pass
            pass
        except Exception:
            return None
        return base64.b64decode(base64_authorization_header).decode('utf-8')
