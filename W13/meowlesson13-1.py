# 2014 final paper
import math
import libdw.sm as sm


# Question 1

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point2D(' + str(self.x) + ',' + str(self.y) + ')'

    def add(self, other):
        newx = self.x + other.dx
        newy = self.y + other.dy
        return Point2D(newx, newy)


class Vector2D:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def length(self):
        return math.sqrt(self.dx ** 2 + self.dy ** 2)


# p = Point2D(1,2)
# v = Vector2D(3,1)
# q = p + v
# print q

class Polyline2D:
    def __init__(self, somepoint, listofvectors):
        self.points = [somepoint]
        self.vectors = []
        for i in range(len(listofvectors)):
            self.points.append(self.points[-1].add(listofvectors[i]))
            self.vectors.append(listofvectors[i])

    def addSegment(self, newvector):
        self.points.append(self.points[-1].add(newvector))
        self.vectors.append(newvector)

    def length(self):
        totallength = 0
        for i in range(len(self.vectors)):
            totallength += self.vectors[i].length()
        return totallength

    def vertex(self, index):
        return self.points[index]


# pline = Polyline2D(Point2D(1,2),[Vector2D(3,1)])
# pline.addSegment(Vector2D(1,0))
# pline.addSegment(Vector2D(0,2))
# print pline.length()
# print pline.vertex(0)
# print pline.vertex(1)
# print pline.vertex(2)
# print pline.vertex(3)

class ClosedPolyline2D(Polyline2D):
    def length(self):
        totallength = 0
        for i in range(len(self.vectors)):
            totallength += self.vectors[i].length()
        totallength += math.sqrt(
            (self.points[0].x - self.points[-1].x) ** 2 + (self.points[0].y - self.points[-1].y) ** 2)
        return totallength


# cpline = ClosedPolyline2D(Point2D(1,2),[Vector2D(3,1)])
# cpline.addSegment(Vector2D(1,0))
# cpline.addSegment(Vector2D(0,2))
# print cpline.length()


# Question 2

class CombLock(sm.SM):
    def __init__(self, keyList):
        self.unlockcode = keyList
        self.currentinp = []

    def getNextValues(self, state, inp):
        if inp == 0:
            out = 'locked'
        elif inp == -1:
            if self.currentinp == self.unlockcode:
                out = 'unlocked'
            else:
                out = 'locked'
            self.currentinp = []
        else:
            self.currentinp.append(inp)
            out = 'locked'
        return self.currentinp, out


# lock = CombLock([1,2,5])
# print lock.transduce([1,2,5,-1])
# print lock.transduce([1,0,2,5,-1])
# print lock.transduce([3,2,5,-1])
# print lock.transduce([1,2,5,-1,1,2,5,-1])
# print lock.transduce([3,2,5,-1,1,2,5,-1])

def mapT2P(x, y):
    if 0 <= x and x <= 3:
        if 0 <= y and y <= 3:
            return 1
        if 4 <= y and y <= 7:
            return 4
        if 8 <= y and y <= 11:
            return 7
    if 4 <= x and x <= 7:
        if 0 <= y and y <= 3:
            return 2
        if 4 <= y and y <= 7:
            return 5
        if 8 <= y and y <= 11:
            return 8
    if 8 <= x and x <= 11:
        if 0 <= y and y <= 3:
            return 3
        if 4 <= y and y <= 7:
            return 6
        if 8 <= y and y <= 11:
            return 9


class TouchMap(sm.SM):
    startState = 0

    def getNextValues(self, state, inp):
        (e, x, y) = inp
        if e == 'TouchUp':
            out = -1
            nextstate = 0
        elif e == 'TouchUpdate':
            if mapT2P(x, y) == state:
                out = 0
                nextstate = state
            else:
                out = mapT2P(x, y)
                nextstate = out
        else:
            out = mapT2P(x, y)
            nextstate = out
        return nextstate, out


m = TouchMap()
print m.transduce([('TouchDown', 2, 2), ('TouchUpdate', 3, 3), ('TouchUp', 4, 4)])
print m.transduce([('TouchDown', 3, 3), ('TouchUpdate', 4, 3), ('TouchUp', 4, 4)])
