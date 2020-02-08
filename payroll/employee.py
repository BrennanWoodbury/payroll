class Employee(object):
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.name.com"

        Employee.num_of_emps += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# class for commission employees
class Commission(Employee):
    def __init__(self, sales, rate):
        self.sales = sales
        self.rate = rate

    # function to compute gross commission over pay period
    def c_pay(self):
        self.sales * self.rate


# class for hourly employees
class Hourly(Employee):
    def __init__(self, pay, hours):
        self.pay = pay
        self.hours = hours

    # function to compute hourly pay and overtime, computes one week at a time
    def h_pay(self):
        if hours > 40:
            return 40 * self.pay + (self.hours - 40) * (self.pay * 1.5)
        else:
            return self.pay * self.hours


# class for salaried employees
class Salary(Employee):
    def __init__(self, pay):
        self.pay = pay

    # function to return semi-weekly pay check
    def s_pay(self):
        return self.pay / 26


# print(emp_1.email)

