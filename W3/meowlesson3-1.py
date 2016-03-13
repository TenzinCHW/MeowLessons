# -*- coding: utf-8 -*-
from math import *

#Homework
#Problem 1
print "Problem 1\n"

def check2(n1, n2, n3, x):
    return x > n1 and x > n2 and x < n3

print "Test case 1: check2(1,4,8,7)"
print "ans = True"
ans = check2(1,4,8,7)
print ans
print '''Test  case 2:  check2 (10,4,8,7) '''
print '''ans = False '''
ans=check2 (10,4,8,7)
print ans
print '''Test  case 3:  check2 (1,10,8,7) '''
print '''ans = False '''
ans=check2 (1,10,8,7)
print ans
print '''Test  case 4:  check2 (1,4,5,7) '''
print '''ans = False '''
ans=check2 (1,4,5,7)
print ans

#Problem 2
print "\n"
print "Problem 2\n"

def cToF(C):
    ans = (C - 32.0)*5.0/9
    return ans

def fToC(F):
    ans = F*9.0/5 + 32.0
    return ans

def tempConvert(CorF, temp):
    if CorF != 'C' and CorF != 'F':
        return None
    elif CorF == 'C':
        return cToF(temp)
    else:
        return fToC(temp)

print "Test case 1: F = 32"
ans=tempConvert('F', 32)
print ans
print "Test case 2: F = -40"
ans=tempConvert('F', -40)
print ans
print "Test case 3: F= 212"
ans=tempConvert('F', 212)
print ans
print "Test case 4: C = 0"
ans=tempConvert('C', 0)
print ans
print "Test case 5: C = -40"
ans=tempConvert('C', -40)
print ans
print "Test case 6: C = 100"
ans=tempConvert('C', 100)
print ans
print "Test case 7: Neither 'C' nor 'F'"
ans=tempConvert('', 0)
print ans
print "Test case 8: Neither 'C' nor 'F'"
ans=tempConvert('A', 0)
print ans

#Problem 3
print "\n"
print "Problem 3\n"

def getEvenNumber(a_list):
    new_list = []
    for i in a_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print 'getEvenNumber([1,2,3,4,5])'
ans=getEvenNumber([1,2,3,4,5])
print ans
print 'getEvenNumber([11,22,33,44,55])'
ans=getEvenNumber([11,22,33,44,55])
print ans
print 'getEvenNumber([10,20,30,40,50])'
ans=getEvenNumber([10,20,30,40,50])
print ans
print 'getEvenNumber([11,21,31,41,51])'
ans=getEvenNumber([11,21,31,41,51])
print ans

#Problem 4
print "\n"
print "Problem 4\n"

def isPrime(integer):
    if integer <= 1:
        return False
    elif integer == 2:
        return True
    else:
        for i in range(2, integer):
            if integer % i != 0:
                pass
            else:
                return False
        return True

print 'isPrime(2)'
ans=isPrime(2)
print ans
print 'isPrime(3)'
ans=isPrime(3)
print ans
print 'isPrime(7)'
ans=isPrime(7)
print ans
print 'isPrime(9)'
ans=isPrime(9)
print ans
print 'isPrime(21)'
ans=isPrime(21)
print ans

#Problem 5
print "\n"
print "Problem 5\n"

def approx_ode(y, h, t0, tn):
    for i in range(int(10*(tn-t0))):
        y += h*(3.0 + e**(-(t0+i*h)) - 0.5*y)
    return y

print "Test Case 1: Input t = 3"
ans = approx_ode(3,0.1)
print "Output: y(3) = %.3f" % ans
print "Test Case 2: Input t = 4"
ans = approx_ode(4,0.1)
print "Output: y(4) = %.3f" % ans
print "Test Case 3: Input t = 5"
ans = approx_ode(5,0.1)
print "Output: y(5) = %.3f" % ans
