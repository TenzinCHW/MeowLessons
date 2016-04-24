# Finals 2015

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
        halflength = inSquare.sideLength/2.0
        x1,y1 = inSquare.x+halflength, inSquare.y+halflength
        x2,y2 = inSquare.x+halflength, inSquare.y-halflength
        x3,y3 = inSquare.x-halflength, inSquare.y + halflength
        x4,y4 = inSquare.x-halflength,inSquare.y-halflength
        return self.containPoint(x1,y1) and self.containPoint(x2,y2) and self.containPoint(x3,y3) and self.containPoint(x4,y4)


s = Square(x=1, y=1, sideLength=2.0)
print s.getCenter()
print s.getSideLength()
print s.getArea()
print s.getPerimeter()
print s.containPoint(0, 0)
print s.containPoint(0, -0.5)
print s.containPoint(1, 1.5)
print s.containSquare(Square(x=1.5, y=1, sideLength=1))
print s.containSquare(Square(x=1.5, y=1, sideLength=1.1))
s2 = Square()
print s2.getCenter()
print s2.getSideLength()
print s2.getPerimeter()

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
