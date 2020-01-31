
#function to calculate total weekly earnings.
def hourly():
    pay_rate = input("Employee's Hourly Wage: ")
    hours = input("Hours worked: ")

    if float(hours) <= 40:
        print( float(hours) * float(pay_rate))
    else:
        print( 40 * float(pay_rate) + (float(hours) - 40) * (float(pay_rate) * 1.5))



hourly()

def test(hourly):
    return hourly * 2

test()