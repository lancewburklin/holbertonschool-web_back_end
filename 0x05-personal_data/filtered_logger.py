#!/usr/bin/env python3
"""
Logging obfuscated info
"""
import re
import logging
from typing import List
import mysql.connector
import os
PII_FIELDS = ('name', 'phone', 'ssn', 'password', 'email')


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


def get_logger() -> logging.Logger:
    """ Create the Logger """
    user_data = logging.getLogger('user_data')
    user_data.propagate = False
    user_data.setLevel(logging.INFO)
    stream_h = logging.StreamHandler()
    stream_h.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    stream_h.setLevel(logging.INFO)
    user_data.addHandler(stream_h)
    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Connecting to mysql """
    uName = os.environ['PERSONAL_DATA_DB_USERNAME'] or 'root'
    uPass = os.environ['PERSONAL_DATA_DB_PASSWORD'] or ""
    dHost = os.environ['PERSONAL_DATA_DB_HOST'] or 'localhost'
    dName = os.environ['PERSONAL_DATA_DB_NAME']
    mydb = mysql.connector.connect(
        host=dHost,
        user=uName,
        password=uPass,
        database=dName
    )
    return mydb
