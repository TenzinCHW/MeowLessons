# TRIANGLE QUIZ
import math


class Triangle:
    def __init__(self, color='green', filled=True, side1=1.0, side2=1.0, side3=1.0):
        self.color = color
        self.filled = filled
        self.side1, self.side2, self.side3 = side1, side2, side3

    def isFilled(self):
        return self.filled

    def setFilled(self, fill):
        self.filled = fill

    def getSide1(self):
        return self.side1

    def getSide2(self):
        return self.side2

    def getSide3(self):
        return self.side3

    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2.0
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area


t = Triangle()
print t.isFilled()
t.setFilled(False)
print t.isFilled()
t = Triangle()
ans = (t.isFilled(), t.getSide1(), t.getSide2(), t.getSide3())
print ans
t = Triangle('red', False, 4.0, 3.0, 5.0)
nans = (t.color, t.isFilled(), t.getSide1(), t.getSide2(), t.getSide3())
print nans
t = Triangle(side1=4.0, side2=3.0, side3=5.0)
ans = t.getArea()
print ans
