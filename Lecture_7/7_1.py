#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

from __future__ import division
from fractions import gcd

class ValueError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        if self.value == 1:
            return "0 denominator"
        else:
            return "ValueError Exception"

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y != 0:
            self.x = x
            self.y = y
        else:
            raise ValueError(1)

    def __str__(self):
        if self.y == 1:
            return str(self.x)
        else:
            return str(self.x) + "/" + str(self.y)

    def __repr__(self):
        return "Frac(x = " + str(self.x) + ", y = " + str(self.y) + ")"

    def __add__(self, other):
        l = self.x*other.y + other.x*self.y
        m = self.y * other.y
        g = gcd(l,m)
        return Frac(l/g, m/g)

    def __sub__(self, other):
        l = self.x*other.y - other.x*self.y
        m = self.y * other.y
        g = gcd(l,m)
        return Frac(l/g, m/g)

    def __mul__(self, other):
        l = self.x * other.x
        m = self.y * other.y
        g = gcd(l,m)
        return Frac(l/g, m/g)
        
    def __truediv__(self, other):
        return self * Frac(other.y,other.x)
        
    # operatory jednoargumentowe
    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __cmp__(self, other):
        sub = self - other
        sub = sub.x / sub.y
        if sub > 0:
            return 1
        elif sub == 0:
            return 0
        elif sub < 0:
            return -1
        else:
            return sub

    def __float__(self):
        return self.x/self.y


# Kod testujący moduł.

import unittest

class TestFrac(unittest.TestCase):
    def setUp(self):
        self.zero = Frac()

    def test_add_frac(self):
        with self.assertRaises(ValueError) as context:
            Frac(1,0) + Frac(2,5)
        self.assertEqual("0 denominator", str(context.exception))
        self.assertEqual(Frac(1,2) + Frac(1,3), Frac(5,6))
        self.assertEqual(Frac(0,1) + Frac(5,6), Frac(5,6))

    def test_sub_frac(self):
        with self.assertRaises(ValueError) as context:
            Frac(1,0) - Frac(2,5)
        self.assertEqual("0 denominator", str(context.exception))
        self.assertEqual(Frac(2,24) - Frac(17,12), Frac(-4,3))
    
    def test_mul_frac(self):
        with self.assertRaises(ValueError) as context:
            Frac(1,0) * Frac(2,5)
        self.assertEqual("0 denominator", str(context.exception))
        self.assertEqual(Frac(2,8) * Frac(4,8), Frac(1,8))
        self.assertEqual(Frac(-2,5) * Frac(1,-6), Frac(1,15))

    def test_div_frac(self):
        with self.assertRaises(ValueError) as context:
            Frac(1,0) / Frac(2,5)
        self.assertEqual("0 denominator", str(context.exception))
        self.assertEqual(Frac(1,10) / Frac(1,5), Frac(1,2))
        self.assertEqual(Frac(-2,5) / Frac(1,-6), Frac(12,5))

    def test_cmp_frac(self):
        self.assertEqual(cmp(Frac(-12,13),Frac(-14,15)),1)
        self.assertEqual(cmp(Frac(12,13),Frac(14,15)),-1)
        self.assertEqual(cmp(Frac(2,4),Frac(32,64)),0)

    def test_frac2float(self):
        self.assertEqual(float(Frac(1,8)),0.125)
        self.assertEqual(float(Frac(-3,12)),-0.25)
        self.assertAlmostEqual(float(Frac(2,3)),0.666,places=2)

    def test_str(self):
        self.assertEqual(str(Frac(1,2)), "1/2")

    def test_repr(self):
        self.assertEqual(repr(Frac(8,9)), "Frac(x = 8, y = 9)")

    def test_pos(self):
        self.assertEqual(+Frac(-1,2), Frac(-1,2))

    def test_neg(self):
        self.assertEqual(-Frac(-2,5), Frac(2,5))

    def test_inv(self):
        self.assertEqual(~Frac(-1,2), Frac(2,-1))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()