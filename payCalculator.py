def calculatePay():  
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    try:
        floatHrs = float(hrs)
    except:
        print("Enter Hours: ")
    rate = input("Enter Rate: ")
    try:
        floatRate = float(rate)
    except:
        print("Enter rate: ")
    if floatHrs > 40:
        overTimeHrs = floatHrs - 40
        regularHrs = 40
    else:
        overTimeHrs = 0
        regularHrs = floatHrs
    pay = regularHrs * floatRate + overTimeHrs * floatRate * 1.5
    print("Pay:", pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()