"""OpenAPI core schemas util module"""
import datetime
from distutils.util import strtobool
from json import dumps
from six import string_types
import phonenumbers


def forcebool(val):
    if isinstance(val, string_types):
        val = strtobool(val)

    return bool(val)


def dicthash(d):
    return hash(dumps(d, sort_keys=True))


def format_date(value):
    return datetime.datetime.strptime(value, '%Y-%m-%d').date()


def format_phone(value):
    try:
        number = phonenumbers.parse(value)
        valid_number = phonenumbers.is_valid_number(number)
        same_value = value is phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
        if not valid_number and same_value:
            raise ValueError
        return value
    except Exception:
        raise ValueError
