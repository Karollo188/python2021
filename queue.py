class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):   # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):   # nigdy nie jest pusta
        return False

    def put(self, data):
        if self.is_full():
            raise TabError("Kolejka jest pelna")
        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise Exception("Kolejka jest pusta")
        return self.items.pop(0)   # mało wydajne!


import unittest

class TestQueue(unittest.TestCase):



    def test_get(self):
        queue = Queue()  # inicjalizacja kolejki
        for item in ["a", 2, 3.5]:
            queue.put(item)
        self.assertEqual(queue.get(), "a")
        self.assertEqual(queue.get(), 2)
        self.assertEqual(queue.get(), 3.5)
        with self.assertRaises(Exception) as context:
            queue.get()
        self.assertTrue("Kolejka jest pusta" in str(context.exception))