#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

import random

class RandomQueue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def insert(self, data):
        if ( self.is_full() ):
            raise ValueError('[Queue.put()] Queue is full.')
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n

    def remove(self):
        if ( self.is_empty() ):
            raise ValueError("[Queue.get()] Queue is empty.")
        else:   
            index = random.randint(0,self.n-1)
            data = self.items[index]
            if index == self.head:
                self.items[self.head] = None      # usuwam referencję
                self.head = (self.head + 1) % self.n
                return data
            elif data == None:
                return self.remove()                     # omit removed element by random and run method again
            else:
                self.items[index] = None          # usuwam referencję
            return data
    
    def printRandomQueue(self):
        for i in self.items:
            print(i)

rq = RandomQueue(3)
rq.printRandomQueue()
rq.insert(1)
rq.insert(2)
rq.insert(3)
print("Po insert")
rq.printRandomQueue()
rq.remove()
rq.remove()
print("Po 2 remove")
rq.printRandomQueue()