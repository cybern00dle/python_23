"""
Services for salary count
"""

from enum import Enum, auto
from collections import namedtuple


Salary = namedtuple(typename='SalaryType', field_names=['amount', 'currency'])


class CURRENCIES(Enum):
    DOLLAR = auto()
    EURO = auto()
    RUBLE = auto()


def convert_to_currency(currency_string: str):
    __rubles = ['RUB', 'rub', 'рубль']
    if currency_string in __rubles:
        return CURRENCIES.RUBLE
    if currency_string == 'DOLLAR':
        return CURRENCIES.DOLLAR
    if currency_string == 'EURO':
        return CURRENCIES.EURO
