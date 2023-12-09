"""
Startup for employee base
"""

from src.employee import *
from src.services import CURRENCIES, Salary


if __name__ == '__main__':

    employee_1 = Programmer('FirstName', 'FirstSurname', 28)
    employee_1_1 = FrontendEngineer('FirstName', 'FirstSurname', 28)
    employee_1_2 = BackendEngineer('FirstName', 'FirstSurname', 28)
    employee_1_3 = QAEngineer('FirstName', 'FirstSurname', 28)

    employee_2 = Manager('SecondName', 'SecondSurname', 65)
    employee_2_1 = CEOManager('SecondName', 'SecondSurname', 65)
    employee_2_2 = HRManager('SecondName', 'SecondSurname', 65)

    employees = [employee_1, employee_1_1, employee_1_2, employee_1_3, employee_2, employee_2_1, employee_2_2]


    # def print_employee_type(empl_obj):
    #     print(f'Does current enployee belong to Employee type? {isinstance(empl_obj, Employee)}')
    #     print(f'Employee {empl_obj.name} is of {type(empl_obj)} type')
    #     print(f"Employee's salary is {empl_obj.get_salary()}")
    #
    #
    # for employee in employees:
    #     print_employee_type(employee)

    salary_obj = Salary(10000, CURRENCIES.RUBLE)
    print(salary_obj)
    print(type(salary_obj))
    print(isinstance(salary_obj, tuple))
    print(salary_obj.amount)
    print(salary_obj.currency)

    empl = Employee('1', '1', 1, Salary(10000, CURRENCIES.RUBLE))
    empl.set_salary(2000, CURRENCIES.DOLLAR)
    print(empl.get_salary(CURRENCIES.RUBLE))
