#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

import random
import math

def randomList(n):
    return random.sample(range(0,n), n)

def almostSorted(n):
    lst = list(range(0,n))
    for i in range(int(n*0.2)):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        lst[a], lst[b] = lst[b], lst[a]
    return lst

def almostSortedReverse(n):
    lst = list(range(0,n))
    for i in range(int(n*0.2)):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        lst[a], lst[b] = lst[b], lst[a]
    lst.reverse
    return lst

def gaussianDistribution(n, mean = 1, sigma = 0.5):
    """Values with Gaussian Distribution with specified mean and standard deviation (sigma)"""
    lst = []
    for n in range(n):
        lst.append(random.gauss(mean, sigma))
    return lst

def repeatedValues(n, k = None):
    """N values from range 0....k where k is ceil(sqrt(n))"""
    k = int(math.ceil(math.sqrt(n)))
    return [random.choice(range(k)) for i in range(10)]