#!/usr/bin/env python3
"""
Logging obfuscated info
"""
import re
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize the function """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.FIELDS = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format a record """
        record.message = filter_datum(self.FIELDS, self.REDACTION,
                                      record.getMessage(), self.SEPARATOR)
        record.asctime = self.formatTime(record)
        return self.formatMessage(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Filter a message """
    for i in fields:
        message = re.sub(f'(?<={i}=).*?(?={separator})', redaction, message)
    return message
