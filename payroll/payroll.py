import sys
from employee import *

emp_1 = Employee("Brennan", "Woodbury", commission, 65000)
emp_2 = Employee("Jeremy", "Pixton", hourly, 65000)

# function to calculate total weekly earnings.
def hourly():

    pay_rate = input("Employee's Hourly Wage: ")
    hours = input("Hours worked: ")
    reg_pay = float(hours) * float(pay_rate)
    otime_pay = 40 * float(pay_rate) + (float(hours) - 40) * (float(pay_rate) * 1.5)

    if float(hours) <= 40:
        return reg_pay
    else:
        return otime_pay


# calculate salaried pay
def salary(pay_rate):
    # pay_rate = input("Employee's Salary: ")
    return pay_rate / 52


def commission(sales, rate):
    return sales * rate


# function to calculate paycheck over 2 weeks.
def pay_check():
    if salary:
        print(round(salary(65039), 2))
    elif hourly:
        hourly() + hourly()
    elif commission:
        print(round(commission(5000, 0.2), 2))


def how_paid():
    answer = str(input("Is employee salary, hourly, or commission?\n")).lower

    if answer == "hourly":
        print(hourly() + hourly())
    elif answer == "commission":
        entry_1 = input("Gross sales: ")
        entry_2 = input("Commission rate(ie .2 or .33): ")
        print(commission(entry_1, entry_2))
    elif answer == "salary":
        sal = input("Salary: ").lower
        print(salary(sal))
    else:
        print("Invalid entry")


# how_paid()
print(emp_1.pay_type)
# print(pay_check())

