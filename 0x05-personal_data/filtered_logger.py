#!/usr/bin/env python3
"""
Logging obfuscated info
"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """ Filter a message """
    for i in fields:
        message = re.sub('(?s)(?<={}=).*?(?={})'.format(i, separator),
                         redaction, message)
    return message
