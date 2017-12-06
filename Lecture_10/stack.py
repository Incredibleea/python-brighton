#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if ( self.is_full() ):
            raise ValueError('[Stack.push()] Stack is full.')
        else:
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if ( self.is_empty() ):
            raise ValueError('[Stack.pop()] Stack is empty.')
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None    # usuwam referencję
            return data