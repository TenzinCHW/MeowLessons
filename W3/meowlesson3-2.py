import math
#Exercises
print "Exercises!\n"

#Exercise 1
print "Exercise 1\n"

def may_Ignore(integer):
    if type(integer) == int:
        return integer + 1
    else:
        return None

print "Test 1: Input = 1"
ans = may_Ignore(1)
print ans
print "Test 2: Input = 1.0"
ans = may_Ignore(1.0)
print ans
print "Test 3: Input = 1+2j"
ans = may_Ignore(1+2j)
print ans
print "Test 1: Input = 'Hello'"
ans = may_Ignore("Hello")
print ans

#Exercise 2
print "\n"
print "Exercise 2\n"

def myReverse(a_list):
    new_list = []
    for i in reversed(a_list):
        new_list.append(i)
    return new_list



#Exercise 3
print "\n"
print "Exercise 3\n"

def piR(n):
    piem1 = 0
    for i in range(n+1):
        piem1 += (2*(2**0.5)/9801)*(math.factorial(4*i) * (1103 + 26390*i))/(((math.factorial(i)) ** 4) * 396 ** (4*i))
    pie = 1/piem1
    return pie

print piR(2)

#Exercise 4

print "\n"
print "Exercise 4\n"

def getGCD(a, b):
    if a% b == 0:
        return min(a, b)
    else:
        return getGCD(b, a%b)

print "\n"
print "Exercise 5 \n"

def simpsonsRule(f, n, a, b):
    h = (b - a)/float(n)
    fa = 0
    fb = 0
    for i in range(1,int(n/2)):
        fa += 2*f(a+2*i*h)
    for i in range(1, int(n/2)+1):
        fb += 4*f(a+(2*i-1)*h)
    approx = h/3.0*(f(a)+f(b)+fa+fb)
    return approx

def f1(x):
    return x**2

def f2(x):
    return math.sin(x)

def f3(x):
    return math.exp(-x)
