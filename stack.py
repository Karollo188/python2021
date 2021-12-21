class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return False

    def push(self, item):
        if self.is_full():
            raise TabError("Stos jest pelen")
        self.items.append(item)         # dodajemy na koniec

    def pop(self):                      # zwraca element
        if self.is_empty():
            raise Exception("Stos jest pusty")
        return self.items.pop()         # zabieram od końca

import unittest

class TestStack(unittest.TestCase):



    def test_pop(self):
        stack = Stack()
        for item in ["a", 2, 3.5]:
            stack.push(item)
        self.assertEqual(stack.pop(), 3.5)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), "a")
        with self.assertRaises(Exception) as context:
            stack.pop()
        self.assertTrue("Stos jest pusty" in str(context.exception))











