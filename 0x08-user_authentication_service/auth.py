#!/usr/bin/env python3
""" Password auth module """
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hash the password """
    password = password.encode('UTF-8')
    password = bcrypt.hashpw(password, bcrypt.gensalt())
    return password
