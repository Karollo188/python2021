import math
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):       # zwraca string "(x, y)"
        return("(" + str(self.x) + "," + str(self.y) + ")")

    def __repr__(self):        # zwraca string "Point(x, y)"
        return ("Point(" + str(self.x) + "," + str(self.y) + ")")

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.



import unittest

class TestPoint(unittest.TestCase):
    def test__str__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        p4 = Point(5, 5)
        self.assertEqual(p1 == Point(1,2), 1)
        self.assertEqual(p1 == Point(3,3), 0)

    def test_length(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        p4 = Point(5, 5)
        self.assertEqual(p2.length(),5)

    def test_cross(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        p4 = Point(5, 5)
        self.assertEqual(p1.cross(p2),-2)
        self.assertEqual(p2.cross(p3),0)

    def test__mult__(self):
        p1 = Point(1,2)
        p2 = Point(3,4)
        p4 = Point(5,5)
        self.assertEqual(p1*p2,11)
        self.assertEqual(p1*p4,15)

    def test__sub__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        self.assertEqual(p1-p2,Point(-2,-2))
        self.assertEqual(p3-p2,Point(0, 0))
    def test__add__(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        p3 = Point(3, 4)
        self.assertEqual(p1 + p2, Point(4, 6))
        self.assertEqual(p3 + p2, Point(6, 8))


if __name__ == '__main__':
    unittest.main()