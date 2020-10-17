class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def __repr__(self):
        return str(self.items)

queue = Queue()
queue.enqueue(1)
print(queue)

queue.enqueue(2)
queue.enqueue(3)
print(queue)

queue.dequeue()
print(queue)