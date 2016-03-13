import math

class Coordinate:
    x = 0
    y = 0

def areaTriangle(p1, p2, p3):
    def side(meow1, meow2):
        woof = math.sqrt((meow1.x - meow2.x)**2 + (meow1.y-meow2.y)**2)
        return woof
    side1 = side(p1, p2)
    side2 = side(p2, p3)
    side3 = side(p3, p1)
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s*(s - side1)*(s - side2)*(s - side3))
    return area
    
print "Test case 1"
p1=Coordinate ()
p1.x=1.5
p1.y=-3.4
p2=Coordinate ()
p2.x=4.6
p2.y=5
p3=Coordinate ()
p3.x=9.5
p3.y=-3.4
ans=areaTriangle(p1 ,p2 ,p3)
print ans

print "Test  Case 2"
p1=Coordinate ()
p1.x=2.0
p1.y=-3.4
p2=Coordinate ()
p2.x=4.6
p2.y=5
p3=Coordinate ()
p3.x=9.5
p3.y=-1.4
ans=areaTriangle(p1 ,p2 ,p3)
print ans

print "Test  Case 3"
p1=Coordinate ()
p1.x=1.5
p1.y=3.4
p2=Coordinate ()
p2.x=4.6
p2.y=5
p3=Coordinate ()
p3.x=-1.5
p3.y=3.4
ans=areaTriangle(p1 ,p2 ,p3)
print ans

print "Test  Case 4"
p1=Coordinate ()
p1.x=-1.5
p1.y=3.4
p2=Coordinate ()
p2.x=4.6
p2.y=5
p3=Coordinate ()
p3.x=4.3
p3.y=-3.4
ans=areaTriangle(p1 ,p2 ,p3)
print ans

p1.x = float(raw_input("Enter x coordinate of the first point of a triangle: "))
p1.y = float(raw_input("Enter y coordinate of the first point of a triangle: "))
p2.x = float(raw_input("Enter x coordinate of the second point of a triangle: "))
p2.y = float(raw_input("Enter y coordinate of the second point of a triangle: "))
p3.x = float(raw_input("Enter x coordinate of the third point of a triangle: "))
p3.y = float(raw_input("Enter y coordinate of the third point of a triangle: "))

ans = areaTriangle(p1, p2, p3)
print "The area of the triangle is %.2f" % ans