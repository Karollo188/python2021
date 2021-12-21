import random

class RandomQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):   # nigdy nie jest pusta
        return False

    def insert(self, item):
        if self.is_full():
            raise TabError("Kolejka jest pelna")
        self.items.append(item)

    def remove(self):
        if self.is_empty():
            raise Exception("Kolejka jest pusta")
        x = random.randrange(len(self.items))
        self.items[len(self.items) - 1], self.items[x] = self.items[x], self.items[len(self.items) - 1]
        return self.items.pop(len(self.items) - 1)

    def clear(self):
        self.items = []


queue = RandomQueue()
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.insert(5)

print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())