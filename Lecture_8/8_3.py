#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

from __future__ import division
import random
import math

POINTS_NO = 10000

def calc_pi( n ):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    inCounter = 0
    for i in range(0, POINTS_NO):
        x = random.random()**2
        y = random.random()**2
        if math.sqrt(x + y) < 1.0:
            inCounter += 1

    return (inCounter / POINTS_NO) * 4

print("Calculated pi:\t\t" + str(calc_pi(POINTS_NO)) + "\nPi from library:\t" + str(math.pi))