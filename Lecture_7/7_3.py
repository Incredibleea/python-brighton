#!/usr/bin/python
# -*- coding: iso-8859-2 -*-s

from __future__ import division

class ValueError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        if self.value == 1:
            return "[ValueError]: Same point exception."
        else:
            return "ValueError Exception"

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1=0, y1=0, x2=1, y2=1):
        if x1 == x2 and y1 == y2:
            raise(ValueError(1))
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

    def intersection(self, other):
        if self.pt1.x <= other.pt1.x and other.pt1.x <= self.pt2.x and self.pt1.y >= other.pt1.y and other.pt1.y >= self.pt2.y:
            return True
        else:
            return False

    def cover(self, other):    # prostąkąt nakrywający oba
        return Rectangle(self.pt1.x, self.pt1.y, other.pt2.x, other.pt2.y)
    def make4(self):
        middle = self.center()
        return [Rectangle(self.pt1.x, self.pt1.y, middle.x, middle.y), Rectangle(self.pt1.x, self.pt2.y, middle.x, middle.y),
                Rectangle(middle.x, middle.y, self.pt2.x, self.pt1.y), Rectangle(middle.x, middle.y, self.pt2.x, self.pt2.y)]

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(0,0,3,3)), "[(0, 0),(3, 3)]")
    
    def test_repr(self):
        with self.assertRaises(ValueError) as context:
            repr(Rectangle(3,3,3,3))
        self.assertEqual("[ValueError]: Same point exception.", str(context.exception))
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

    def test_intersection(self):
        self.assertFalse(Rectangle(0,0,3,3).intersection(Rectangle(4,4,8,8)))
        self.assertTrue(Rectangle(6,6,8,2).intersection(Rectangle(7,5,1,-17)))

    def test_dummycover(self):
        self.assertEqual(Rectangle(0,3,3,0).cover(Rectangle(3,0,6,-3)), Rectangle(0,3,6,-3))

    def test_dummymake4(self):
        self.assertEqual(Rectangle(0,4,4,0).make4(), [Rectangle(0,4,2,2), Rectangle(0,0,2,2), Rectangle(2,2,4,4), Rectangle(2,2,4,0)])

if __name__ == "__main__":
    unittest.main()