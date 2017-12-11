#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

from __future__ import division

def solve1(a, b, c):
    """Rozwiazywanie rownania liniowego a * x + b * y + c = 0."""

    print("Rozwiaznie rownania liniowego " + str(a) + " * x + " + str(b) + " * y + " + str(c) + " = 0")
    if a == 0:
        if b == 0 and c == 0:
            print("0 * x + 0 * y + 0 = 0 => nieskonczenie wiele rozwiazan")
        elif b == 0 and c != 0:
            print("0 * x + 0 * y + " + str(c) + " = 0 => brak rozwiazan")
        else:
            print("x = 0 , y = " + str(-c / b))
    else:
        if b == 0:
            print("x = " + str(-c/a) + ", y = 0".format(-c/a))
        elif b != 0 and c == 0:
            print("y = " + str(-b/a) + " * x")
        else:
            print("y = " + str(-b/a) + " * x - " + str(c))

solve1(0, 0, 0)
solve1(0, 0 ,8)
solve1(0, 4, 7)
solve1(4, 3, 0)
solve1(9, 0 ,7)
solve1(1, 3, 0)
solve1(1, 2, 3)