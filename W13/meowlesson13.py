# Finals 2015
from libdw import sm


# Question 3

def compTrace(A):
    meow = 0
    total = 0
    for i in range(len(A[0])):
        total += A[meow][meow]
        meow += 1
    return total


# A = [[2.2, 2, 3.1], [4, 5, 6], [7, 8, 9]]
# print compTrace(A)


# Question 4
def findKey(dInput, strInput):
    finallist = []
    for key, value in dInput.iteritems():
        if value == strInput:
            finallist.append(key)
    return sorted(finallist)


# dInput = {1:'singapore',20:'china',4:'japan',5:'china',10:'japan'}
# print findKey(dInput,'china')
# print findKey(dInput,'korea')

# Question 5
class Square():
    def __init__(self, x=0.0, y=0.0, sideLength=1.0):
        self.x = float(x)
        self.y = float(y)
        self.sideLength = float(sideLength)

    def getCenter(self):
        return self.x, self.y

    def getSideLength(self):
        return self.sideLength

    def getArea(self):
        return self.sideLength ** 2

    def getPerimeter(self):
        return 4 * self.sideLength

    def containPoint(self, px, py):
        return abs(self.x - px) <= self.sideLength / 2 and abs(self.y - py) <= self.sideLength / 2

    def containSquare(self, inSquare):
        halflength = inSquare.sideLength / 2.0
        x1, y1 = inSquare.x + halflength, inSquare.y + halflength
        x2, y2 = inSquare.x + halflength, inSquare.y - halflength
        x3, y3 = inSquare.x - halflength, inSquare.y + halflength
        x4, y4 = inSquare.x - halflength, inSquare.y - halflength
        return self.containPoint(x1, y1) and self.containPoint(x2, y2) and self.containPoint(x3,
                                                                                             y3) and self.containPoint(
            x4, y4)


# s = Square(x=1, y=1, sideLength=2.0)
# print s.getCenter()
# print s.getSideLength()
# print s.getArea()
# print s.getPerimeter()
# print s.containPoint(0, 0)
# print s.containPoint(0, -0.5)
# print s.containPoint(1, 1.5)
# print s.containSquare(Square(x=1.5, y=1, sideLength=1))
# print s.containSquare(Square(x=1.5, y=1, sideLength=1.1))
# s2 = Square()
# print s2.getCenter()
# print s2.getSideLength()
# print s2.getPerimeter()

# (1.0, 1.0)
# 2.0
# 4.0
# 8.0
# True
# False
# True
# True
# False
# (0.0, 0.0)
# 1.0
# 4.0


class Elevator(sm.SM):
    startState = 'First'

    def getNextValues(self, state, inp):
        if state == 'First':
            if inp == 'Up':
                nextstate = 'Second'
            else:
                nextstate = 'First'
        elif state == 'Second':
            if inp == 'Up':
                nextstate = 'Third'
            else:
                nextstate = 'First'
        else:
            if inp == 'Up':
                nextstate = 'Third'
            else:
                nextstate = 'Second'
        return nextstate, nextstate


# e = Elevator()
# print e.transduce(['Up','Up','Up','Up','Down','Down','Down','Up'])

# Question 7

def countNumOpenLocker(K):
    lockers = []  # Creates a list of lockers
    for i in range(K):
        lockers.append('c')  # Add on K lockers, all closed.

    for i in range(1, K + 1):  # For every single locker
        for j in range(i - 1, K, i):  # Start at the i-th locker, and increment by i each time through this loop
            if lockers[j] == 'o':
                lockers[j] = 'c'  # Close the locker if it's open
            else:
                lockers[j] = 'o'  # Open the locker if it's closed
    return lockers.count('o')


print countNumOpenLocker(1000000)
