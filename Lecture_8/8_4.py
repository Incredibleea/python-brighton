#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

from __future__ import division
import math

def heron( a, b, c ):
    """Obliczanie pola powierzchni trojkata za pomoca wzoru Herona. Dlugosci bokow trojkata wynosza a, b, c."""
    if (a == 0 or b == 0 or c == 0) or a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('Values: (' + str(a) + ", " + str(b) + ", " + str(c) +
                         ") doesn't meet triangle condition.")
    else:
        p = (a + b + c) / 2
        pole = p * (p - a) * (p - b) * (p - c)
        print("Pole trojkata: ( {}, {}, {} ) = {}".format(a, b, c, math.sqrt(pole)))

try:
    heron(1,2,3)
except ValueError as e:
    print(e.message)

heron(2,4,3)
heron(3,4,5)
heron(4,4,7)