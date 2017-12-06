#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

import stack
import unittest

class TestStack(unittest.TestCase):
    def test_is_empty(self):
        st = stack.Stack(3)
        self.assertTrue(st.is_empty())
        st.push(6)
        self.assertFalse(st.is_empty())
        st.pop()
        self.assertTrue(st.is_empty())

    def test_is_full(self):
        st = stack.Stack(3)
        self.assertFalse(st.is_full())
        for i in range(3):
            st.push(3)
        self.assertTrue(st.is_full())
        st.pop()
        self.assertFalse(st.is_full())

    def test_push(self):
        st = stack.Stack(3)
        a = "random string"
        st.push(a)
        self.assertEqual(a, st.pop())
        for i in range(3):
            st.push(4)
        with self.assertRaises(ValueError) as context:
            st.push(5)
        self.assertEqual("[Stack.push()] Stack is full.", str(context.exception))

    def test_pop(self):
        st = stack.Stack(3)
        a = 14
        st.push(a)
        self.assertEqual(a, st.pop())
        with self.assertRaises(ValueError) as context:
            st.pop()
        self.assertEqual("[Stack.pop()] Stack is empty.", str(context.exception))

if __name__ == "__main__":
    unittest.main()