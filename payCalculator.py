def calculatePay():  
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    hrs = float(hrs)
    rate = input("Enter Rate: ")
    rate = float(rate)
    if hrs > 40:
        overTimeHrs = hrs - 40
        regularHrs = 40
    else:
        overTimeHrs = 0
        regularHrs = hrs
    pay = regularHrs * rate + overTimeHrs * rate * 1.5
    print("Pay:", pay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()