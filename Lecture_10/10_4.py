#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

import queue
import unittest

class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        que = queue.Queue(3)
        self.assertTrue(que.is_empty())
        que.put(1)
        self.assertFalse(que.is_empty())
        que.get()
        self.assertTrue(que.is_empty())

    def test_is_full(self):
        que = queue.Queue(3)
        self.assertFalse(que.is_full())
        for i in range(3):
            que.put(1)
        self.assertTrue(que.is_full())
        que.get()
        self.assertFalse(que.is_full())

    def test_put(self):
        que = queue.Queue(3)
        a = "random string"
        que.put(a)
        self.assertEqual(a, que.get())
        for i in range(3):
            que.put(1)
        with self.assertRaises(ValueError) as context:
            que.put(5)
        self.assertEqual("[Queue.put()] Queue is full.", str(context.exception))

    def test_get(self):
        que = queue.Queue(3)
        a = 11
        que.put(a)
        self.assertEqual(a, que.get())
        with self.assertRaises(ValueError) as context:
            que.get()
        self.assertEqual("[Queue.get()] Queue is empty.", str(context.exception))

if __name__ == "__main__":
    unittest.main()