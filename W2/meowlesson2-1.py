amount = float(raw_input('Enter the monthly saving amount: '))
interest = float(raw_input('Enter annual interest rate: '))

def Compoundint(amt, interest, months):
    monthlyint = interest/12.0 #Interest rate for each month
    total = 0 #Initialize balance
    for i in range(months): #Loop over each month
        total = (total + amt)*(1+monthlyint) #Add amt to the balance, then multiply by the monthly interest rate each month
    return total

a = Compoundint(amount, interest, 6)
print "After the sixth month, the account value is %.2f" % a