#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

# P(0, 0) = 0.5,
# P(i, 0) = 0.0 dla i > 0,
# P(0, j) = 1.0 dla j > 0,
# P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.

import time

R = {}

def dynamic( i, j ):
    D = {}
    start = time.clock()
    for i in range( i + 1 ):
        for j in range( j + 1 ):
            if i == 0 and j == 0:
                D[ (i,j) ] = 0.5
            elif i > 0 and j == 0:
                D[ (i,j) ] = 0.0
            elif i == 0 and j > 0:
                D[ (i,j) ] = 1.0
            else:
                D[ (i,j) ] = 0.5 * ( D[ (i-1,j) ] + D[ (i,j-1) ]) 
    stop = time.clock()
    print("Dynamic time:\t" + str(stop - start))
    return D

def recursive(i, j):
    if i == 0 and j == 0:
        R[ (i,j) ] = 0.5
        return 0.5
    elif i > 0 and j == 0:
        R[ (i,j) ] = 0.0
        return 0
    elif i == 0 and j > 0:
        R[ (i,j) ] = 1.0
        return 1
    if j > 0 and i > 0:
        R[ (i,j) ] = ( recursive(i - 1, j) + recursive(i, j - 1)) / 2
        return 0.5 * ( recursive(i - 1, j) + recursive(i, j - 1) )

i = 2
j = 3
print("i = {}, j = {}\n".format(i,j))

dynamic(i, j)

start = time.clock()
recursive(i, j)
stop = time.clock()
print("Recursive time:\t" + str(stop - start))