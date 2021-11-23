print("Zestaw 6")

from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return("[" + str(self.pt1.__str__()) + ", " + str(self.pt2.__str__()) + "]")

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return ("Rectangle" + str(self.__str__()))

    def __eq__(self, other):    # obsługa rect1 == rect2
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        x = (self.pt1.x + self.pt2.x) / 2
        y = (self.pt1.y + self.pt2.y) / 2
        return Point(x,y)

    def area(self):             # pole powierzchni
        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

    def move(self, x, y):       # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

# Kod testujący moduł.

import unittest

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(3, 4)
p4 = Point(5, 5)

r1 = Rectangle(p1.x,p1.y,p2.x,p2.y)
r2 = Rectangle(p1.x,p1.y,p3.x,p3.y)
r3 = Rectangle(p3.x,p3.y,p4.x,p4.x)

class TestRectangle(unittest.TestCase):
    def test__str__(self):
        self.assertEqual(r1 == Rectangle(1,2,3,4), 1)
        self.assertEqual(r3 == Rectangle(1,2,3,4), 0)

    def test__eq__(self):
        self.assertEqual(r1 == r2, 1)
        self.assertEqual(r1 == r3, 0)

    def test__ne(self):
        self.assertEqual(r1 != r2, 0)
        self.assertEqual(r1 != r3, 1)

    def test_center(self):
        self.assertEqual(r1.center() == Point(2,3), 1)
        self.assertEqual(r1.center() == Point(2, 5), 0)

    def test_area(self):
        self.assertEqual((r1.area() == 4), 1)
        self.assertEqual((r3.area() == 2), 1)

    def test_move(self):
        r1.move(1, 2)
        self.assertEqual(r1 == Rectangle(2,4,4,6), 1)
        r1.move(1,1)
        self.assertEqual(r1 == Rectangle(2, 4, 4, 6), 0)

if __name__ == '__main__':
    unittest.main()