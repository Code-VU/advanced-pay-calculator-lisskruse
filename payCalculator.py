def calculatePay():  
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    try:
        global floatHrs = float(hrs)
        if floatHrs > 40:
            global overTimeHrs = floatHrs - 40
            global regularHrs = 40
        else:
            global overTimeHrs = 0
            global regularHrs = floatHrs
    except:
        print("Please enter a number.")
    rate = input("Enter Rate: ")
    try:
        global floatRate = float(rate)
    except:
        print("Please enter a number.")
    pay = regularHrs * floatRate + overTimeHrs * floatRate * 1.5
    print("Pay:", pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()