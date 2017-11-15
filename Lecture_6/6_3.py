#!/usr/bin/python
# -*- coding: iso-8859-2 -*-s

from __future__ import division

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[(" + str(self.pt1.x) + ", " + str(self.pt1.y) + "),(" \
            + str(self.pt2.x) + ", " + str(self.pt2.y) + ")]"

    def __repr__(self):
        return "Rectangle(x1 = " + str(self.pt1.x) + ", x2 = " + str(self.pt1.y) \
            + ", y1 = " + str(self.pt2.x) + ", y2 = " + str(self.pt2.y) + ")"

    def __eq__(self, other):
        return (self.pt1.x == other.pt1.x) and (self.pt1.y == other.pt1.y) \
            and (self.pt2.x == other.pt2.x) and (self.pt2.y == other.pt2.y) \
            or (self.pt1.x == other.pt2.x) and (self.pt1.y == other.pt2.y) \
            and (self.pt2.x == other.pt1.x) and (self.pt2.y == other.pt1.y)


    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return (abs(self.pt2.x - self.pt1.x)) * (abs(self.pt2.y - self.pt1.y))

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(0,0,3,3)), "[(0, 0),(3, 3)]")
    
    def test_repr(self):
        self.assertEqual(repr(Rectangle(0,0,3,3)), "Rectangle(x1 = 0, x2 = 0, y1 = 3, y2 = 3)")

    def test_eq(self):
        self.assertTrue(Rectangle(0,0,3,3) == Rectangle(0,0,3,3))
        self.assertTrue(Rectangle(3,3,0,0) == Rectangle(0,0,3,3))
        self.assertFalse(Rectangle(0,0,3,3) == Rectangle(0,1,3,3))
    
    def test_ne(self):
        self.assertFalse(Rectangle(0,0,3,3) != Rectangle(0,0,3,3))
        self.assertFalse(Rectangle(3,3,0,0) != Rectangle(0,0,3,3))
        self.assertTrue(Rectangle(0,0,3,3) != Rectangle(0,1,3,3))

    def test_center(self):
        self.assertTrue(Rectangle(3,3,0,0).center(), Point(1.5,1.5))

    def test_area(self):
        self.assertEqual(Rectangle(3,3,0,0).area(), 9)
        self.assertEqual(Rectangle.area(Rectangle(3,3,0,0)), 9)
    
    def test_move(self):
        self.assertTrue(Rectangle(0,0,3,3).move(4,5), Rectangle(4,4,8,8))

if __name__ == "__main__":
    unittest.main()