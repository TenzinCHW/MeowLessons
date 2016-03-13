amount = float(raw_input('Enter the monthly saving amount: '))
interest = float(raw_input('Enter annual interest rate: '))

def Compoundint(amt, interest, months):
    monthlyint = interest/12.0
    total = 0
    for i in range(months):
        total = (total + amt)*(1+monthlyint)
    return total

a = Compoundint(amount, interest, 6)
print "After the sixth month, the account value is %.2f" % a