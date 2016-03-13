#Quiz C - The long one
def isValid(number):
    if getSize(number) < 13 or getSize(number) > 16 or (getPrefix(number,1) not in [4,5,6] and getPrefix(number,2) not in [37]):
        return False
    elif (sumOfDoubleEvenPlace(int(number)) + sumOfOddPlace(int(number)))%10 == 0:
        return True
    return False

def prefixMatched(number, d):
    return str(d) in str(number)[:len(str(d))]

def getSize(d):
    return len(str(d))

def getPrefix(number,k):
    if len(str(number)) < len(str(k)):
        return int(number)
    else:
        return int(str(number)[:k])
# Get the result from Step 2.
def sumOfDoubleEvenPlace(number):
    sumDE=0
    while number!=0:
        number/=10
        digit=number%10
        double=digit*2
        digitSum=getDigit(double)
        sumDE+=digitSum
        number/=10
    return sumDE

# Return this number if it is a single digit, othewise, return the sum of the two digits.
def getDigit(number):
    if number<10:
        return number
    else:
        return (number/10+number%10)

# Return sum of odd place digits in number. Assume given.
def sumOfOddPlace(number):
    sumDE=0
    while number!=0:
        digit=number%10
        sumDE+=digit
        number/=100
    return sumDE

# print getPrefix(4388576018402626,1)
# print getPrefix(4388576018402626,2)
# print prefixMatched(4388576018402626,4)
# print prefixMatched(4388576018402626,5)
# print prefixMatched(4388576018402626,43)

print isValid(4388576018402626)
print isValid(4388576018410707)
print isValid(371826291433349)
print isValid(5411045872559122)
print isValid(6011432717792989)
