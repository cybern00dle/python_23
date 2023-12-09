"""
Employee
"""

from src.services import CURRENCIES, Salary
from datetime import datetime


class Date:

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = datetime.strptime(value, '%Y:%m:%d')


class Employee:

    birth_date = Date()

    def __init__(self, name, surname, age, birth_date='2020:12:23', salary: Salary | None = None):
        self.name = name # вызывается сеттер
        self.surname = surname
        self.age = age # вызывается сеттер
        self.__salary = salary
        self.birth_date = birth_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name.upper()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def print_initials(self):
        print(f'Name: {self.name}, Surname: {self.surname}, Age: {self.age}')

    @staticmethod
    def say_hello(self):
        # реализовать статические методы или нет зависит от того насколько он вообще связан с классом
        # его можно вынести вне класса и обращаться к нему внутри класса
        print('Hello!')

    def __count_salary(self, currency):
        match (currency, self.__salary.currency):
            case (CURRENCIES.RUBLE, CURRENCIES.DOLLAR): return self.__salary.amount * 88
            case (CURRENCIES.DOLLAR, CURRENCIES.RUBLE): return self.__salary.amount / 88
            case _: raise AttributeError

    def set_salary(self, amount, currency):
        self.__salary = Salary(amount, currency)

    def get_salary(self, currency=CURRENCIES.RUBLE):
        if self.__salary and (currency == self.__salary.currency):
            return self.__salary.amount
        return self.__count_salary(currency)


class Programmer(Employee):
    pass


class Manager(Employee):
    pass


class CEOManager(Manager):
    pass


class HRManager(Manager):
    pass


class FrontendEngineer(Programmer):
    pass


class BackendEngineer(Programmer):
    pass


class QAEngineer(Programmer):
    pass
