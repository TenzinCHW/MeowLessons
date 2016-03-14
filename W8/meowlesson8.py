# Cohort 8
import math
import time
import numpy


# Problem 1
class Coordinate:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getXY(self):
        return self.x, self.y

    def getMagnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


# Problem 2
class Square:
    def __init__(self, side):
        self.side = side

    def getArea(self):
        area = self.side ** 2
        return float(area)

    def setArea(self, area):
        self.side = math.sqrt(area)
        if self.side % 1 == 0:
            return int(self.side)
        else:
            return float(self.side)

    def __str__(self):
        return "Square of height and width " + str(self.side) + "."


# Problem 3

class StopWatch:
    def __init__(self):
        self.startTime = time.time()
        self.endTime = -1

    def start(self):
        self.startTime = time.time()
        self.endTime = -1

    def stop(self):
        self.endTime = time.time()

    def getElapsedTime(self):
        if self.endTime == -1:
            return None
        else:
            return int((self.endTime - self.startTime) * 1000)

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime


# Problem 4

class Line:
    def __init__(self, c0, c1): #Initializes c0 and c1 of the class
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x): #Makes instance of class callable as a function
        return round(self.c0 + self.c1 * x,1) #This is what will happen if you do something like...
    #thisline = Line()
    #thisline(5) <<< the function will operate on the argument passed in as x.

    def table(self, startx, endx, n):
        tableau = '' #Initialize a table. I'm calling it tableau, I think it's French.
        if n == 0:
            return 'Error in printing table' # Case if n = 0
        elif startx == endx:
            return '%10.2f' %(startx) + '%10.2f' %(self.c0+self.c1*startx) + '\n' #Case if start and end are the same
        else:
            for i in numpy.linspace(startx, endx, n): #All other cases. Creates an array w start @ startx and end @ endx. Contains n points.
                tableau += '%10.2f' % (float(i)) + '%10.2f' % (self.c0+self.c1*i) + '\n' #This is basic string formatting. f means float, 10 is the no. of charactaers, .2 means 2 dp.
            return tableau

def testLine(c0,c1,x,L,R,N):
    line=Line(c0,c1)
    return line(x),line.table(L,R,N)
print testLine(1,2,2,1,5,4)
