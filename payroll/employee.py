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

    def fullname(self):
        print(self.first + " " + self.last)


# class for commission employees
class Commission(Employee):

    def __init__(self, first, last, sales, rate):
        super().__init__(first, last)
        self.sales = sales
        self.rate = rate

    # function to compute gross commission over pay period
    def c_pay(self):
        return self.sales * self.rate


# class for hourly employees
class Hourly(Employee):

    def __init__(self, first, last, pay, hours):
        super().__init__(first, last)
        self.pay = pay
        self.hours = hours

    # function to compute hourly pay and overtime, computes one week at a time
    def h_pay(self):
        if self.hours > 40:
            return 40 * self.pay + (self.hours - 40) * (self.pay * 1.5)
        else:
            return self.pay * self.hours


# class for salaried employees
class Salary(Employee):
    def __init__(self, first, last, pay):
        super().__init__(first, last)
        self.pay = pay

    # function to return semi-weekly pay check
    def s_pay(self):
        return self.pay / 26


# print(emp_1.email)

emp_1 = Hourly("Brennan", "Woodbury", 22, 45)
emp_2 = Commission("Jeremy", "Pixton", 5000, .2)
emp_3 = Salary("Abigayle", "Egbert", 65000)


print(emp_3.s_pay())