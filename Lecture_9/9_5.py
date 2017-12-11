#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

class Node:
    """Klasa reprezentująca węzeł listy dwukierunkowej."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DoubleList:
    """Klasa reprezentująca całą listę dwukierunkową."""

    def __init__(self):
        self.length = 0   # może to trzymać w polu data wartownika?
        self.nil = Node()   # wartownik
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def is_empty(self):
        # return self.length == 0
        return self.nil.next == self.nil

    def count(self):
        return self.length

    def insert_head(self, data):
        node = Node(data)
        node.next = self.nil.next
        node.prev = self.nil
        self.nil.next.prev = node
        self.nil.next = node
        self.length += 1

    def insert_tail(self, data):
        node = Node(data)
        node.next = self.nil
        node.prev = self.nil.prev
        self.nil.prev.next = node
        self.nil.prev = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise Exception("pusta lista")
        node = self.nil.next
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node.data

    def remove_tail(self):
        if self.is_empty():
            raise Exception("pusta lista")
        node = self.nil.prev
        # Teraz ogólny schemat usuwania węzła.
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        return node.data

    def remove_max(self):
        if self.is_empty():
            raise Exception("pusta lista")
        nodemax = self.nil.next
        maxdata = self.nil.next.data
        iterator = self.nil
        for i in range(self.count()-1):
            iterator = iterator.next
            if iterator.data > maxdata:
                nodemax = iterator
                maxdata = iterator.data

        nodemax.prev.next = nodemax.next
        nodemax.next.prev = nodemax.prev
        self.length -= 1

        return nodemax

    def remove_min(self):
        if self.is_empty():
            raise Exception("pusta lista")
        nodemin = self.nil.next
        mindata = self.nil.next.data
        iterator = self.nil
        for i in range(self.count()-1):
            iterator = iterator.next
            if iterator.data < mindata:
                nodemin = iterator
                mindata = iterator.data

        nodemin.prev.next = nodemin.next
        nodemin.next.prev = nodemin.prev
        self.length -= 1
        
        return nodemin

# Kod testujący moduł.

import unittest

class TestDoubleList(unittest.TestCase):
    def setUp(self):
        self.zero = DoubleList()

    def test_max(self):
        dl = DoubleList()
        dl.insert_head(3)
        dl.insert_head(66)
        dl.insert_head(12)
        self.assertEquals(66, dl.remove_max().data)

    def test_min(self):
        dl2 = DoubleList()
        dl2.insert_head(3)
        dl2.insert_head(1)
        dl2.insert_head(12)
        self.assertEquals(1, dl2.remove_min().data)

if __name__ == '__main__':
    unittest.main()