import sys
from employee import *

#function to calculate total weekly earnings.
def hourly():
    
    pay_rate = input("Employee's Hourly Wage: ")
    hours = input("Hours worked: ")
    reg_pay = float(hours) * float(pay_rate)
    otime_pay = 40 * float(pay_rate) + (float(hours) - 40) * (float(pay_rate) * 1.5)


    if float(hours) <= 40:
        return(reg_pay)
    else:
        return(otime_pay)
    
#calculate salaried pay    
def salary():
    pass



#function to calculate paycheck over 2 weeks. 
def pay_check():

    return(hourly() + hourly())
    
    
print(emp_1.first)
print(pay_check())






