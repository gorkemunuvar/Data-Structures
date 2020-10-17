class Deque(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def __repr__(self):
        return str(self.items)


deque = Deque()

deque.add_front(1)
print(deque)

deque.add_front(2)
deque.add_front(3)
print(deque)

deque.add_rear(5)
print(deque)

deque.remove_rear()
print(deque)

deque.remove_front()
print(deque)
