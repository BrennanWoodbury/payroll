
#function to calculate total weekly earnings.
def hourly_1():
    
    pay_rate = input("Employee's Hourly Wage: ")
    hours = input("Hours worked: ")
    reg_pay = float(hours) * float(pay_rate)
    otime_pay = 40 * float(pay_rate) + (float(hours) - 40) * (float(pay_rate) * 1.5)


    if float(hours) <= 40:
        print(reg_pay)
    else:
        print(otime_pay)
    return
     

hourly_1()

#function to calculate total weekly earnings.
def hourly_2():
    
    pay_rate = input("Employee's Hourly Wage: ")
    hours = input("Hours worked: ")
    reg_pay = float(hours) * float(pay_rate)
    otime_pay = 40 * float(pay_rate) + (float(hours) - 40) * (float(pay_rate) * 1.5)


    if float(hours) <= 40:
        print(reg_pay)
    else:
        print(otime_pay)
    return
        

hourly_2()

#function to calculate paycheck over 2 weeks. 
def pay_check(hourly_1, hourly_2):
    hourly_1 = {}
    hourly_2 = {}

    print(hourly_1 + hourly_2)
    return
    

pay_check()
