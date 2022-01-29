def calculatePay():  
    # This first line is provided for you
    floatHrs = float(0)
    overTimeHrs = float(0)
    regularHrs = float(0)
    floatRate = float(0)
    hrs = input("Enter Hours: ")
    try:
        floatHrs = float(hrs)
        if floatHrs > 40:
            overTimeHrs = floatHrs - 40
            regularHrs = 40
        else:
            overTimeHrs = 0
            regularHrs = floatHrs
        pay = regularHrs * floatRate + overTimeHrs * floatRate * 1.5
        print("Pay:", pay)
    except:
        print("Error, please enter numeric input")
    rate = input("Enter Rate: ")
    try:
        floatRate = float(rate)
        pay = regularHrs * floatRate + overTimeHrs * floatRate * 1.5
        print("Pay:", pay)
    except:
        print("Error, please enter numeric input")
        # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()