#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

# Istota algorytmu jest struktura kopca ktora zaklada, że
# węzeł nadrzędny jest większy lub równy węzłom potomnym.
# Algotrytm ten ma zlozonosc obliczeniowa O(n logn).

import random

import ListGenerator as getter

def updateHeap(lst, end, i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and lst[i] < lst[l]:   
        max = l   
    if r < end and lst[max] < lst[r]:   
        max = r   
    if max != i:   
        lst[i], lst[max] = lst[max], lst[i]     # swap leaves
        updateHeap(lst, end, max)   
 
def heapSort(lst):     
    end = len(lst)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        updateHeap(lst, end, i)   
    for i in range(end-1, 0, -1):   
        lst[i], lst[0] = lst[0], lst[i]         # swap leaves   
        updateHeap(lst, i, 0)   

listToSort = getter.randomList(10)
print(listToSort)
heapSort(listToSort)
print(listToSort)

print("\n\nTest ListGenerator module")

print("getter.randomList:   ", getter.randomList(10))
print("getter.almostSorted: ", getter.almostSorted(10))
print("getter.almostSortedReverse: ", getter.almostSortedReverse(10))
print("getter.gaussianDistribution: ", getter.gaussianDistribution(10, 2, 0.8))
print("getter.repeatedValues: ", getter.repeatedValues(10))