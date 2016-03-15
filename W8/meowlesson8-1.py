# Homework week 8
from math import *


# Problem 1
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setTime(self, elapseTime):  # Start from 0
        self.second = elapseTime % 60  # Take remainder after dividing by 60
        self.minute = elapseTime // 60 % 60  # Take remainder after dividing by 60*60
        self.hour = elapseTime // 3600 % 12  # Take remainder after dividing by 12*60*60


# t = Time(5, 30, 23)
# ans = (t.getHour(), t.getMinute(), t.getSecond())
# print ans
# t.setTime(555550)
# ans = (t.getHour(), t.getMinute(), t.getSecond())
# print ans

# thetime = Time(2, 4, 24)
# thetime.setTime(55550)
# print thetime.getHour(), thetime.getMinute(), thetime.getSecond()

# Problem 2
class Account:
    def __init__(self, name, accnum, initbal):
        self.name = name
        self.accnum = accnum
        self.bal = initbal

    def __str__(self):
        return '%s,' % self.name + ' %s,' % self.accnum + ' balance: %s' % (str(self.bal))

    def deposit(self, amt):
        self.bal += amt

    def withdraw(self, amt):
        self.bal -= amt


# a1 = Account('John Olsson', '19371554951', 20000)
# a2 = Account('Liz Olsson', '19371564761', 20000)
# a1.deposit(1000)
# a1.withdraw(4000)
# a2.withdraw(10500)
# a1.withdraw(3500)
# print a1
# print a2

# Problem 3
# return only the derivative value without rounding
# your return value is a float, which is the approximate value of the derivative
# Tutor will compute the approximate error based on your return value

class Diff:
    def __init__(self, effex, h=1E-2):
        self.effex = effex
        self.haich = h

    def __call__(self, x):
        differential = (self.effex(x + self.haich) - self.effex(x)) / self.haich
        return differential


# Problem 4
# For Test case 2: return a tuple with coeff list and evaluated value

class Polynomial:
    def __init__(self, coeffs):
        self.coeff = coeffs

    def __add__(self, other):
        if len(self.coeff) > len(other.coeff):
            summa = self.coeff[:]
            for i in range(len(other.coeff)):
                summa[i] += other.coeff[i]
        else:
            summa = other.coeff[:]
            for i in range(len(self.coeff)):
                summa[i] += self.coeff[i]
        return summa

    def __sub__(self, other):
        if len(self.coeff) > len(other.coeff):
            summa = self.coeff[:]
            for i in range(len(other.coeff)):
                summa[i] -= other.coeff[i]
        else:
            summa = other.coeff[:]
            for i in range(len(other.coeff) - len(self.coeff)):
                self.coeff.append(0)
            for i in range(len(summa)):
                summa[i] = self.coeff[i] - summa[i]
        subtracted = Polynomial(summa)  # They want the sub method to return an instance of the class Polynomial
        return subtracted  # The instance will use summa as its coeffs input

    def __call__(self, x):
        ans = 0
        for i in range(len(self.coeff)):
            ans += self.coeff[i] * x ** i
        return ans

    def __mul__(self, other):
        multi = []
        for i in range(len(self.coeff) + len(other.coeff) - 1):
            multi.append(0)
        for i in range(len(other.coeff)):
            for j in range(len(self.coeff)):
                multi[i + j] += self.coeff[j] * other.coeff[i]
        return multi

    def differentiate(self):
        newcoeff = self.coeff[1:]
        for i in range(len(newcoeff)):
            newcoeff[i] = newcoeff[i] * (i + 1)
        self.coeff = newcoeff[:]

    def derivative(self):
        newcoeff = self.coeff[1:]
        for i in range(len(newcoeff)):
            newcoeff[i] = newcoeff[i] * (i + 1)
        return Polynomial(newcoeff)


meow = Polynomial([1, 1])
woof = Polynomial([0, 1, 0, 0, -6, -1])
rawr = Polynomial(meow - woof)
print (rawr.coeff, rawr(3))
# a = Polynomial([1,2,3])
# b = Polynomial([3,2,1])
# print a+b
# print a-b
# print a*b
