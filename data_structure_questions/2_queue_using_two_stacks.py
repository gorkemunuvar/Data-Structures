# Problem: Given the Stack class below, implement a Queue class using two stacks!
# Note: Note that you should use list like stacks. For example you should avoid
# using list.insert() function.

class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if self.is_empty():
            return 'Empty Queue'

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        result = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return result

    def is_empty(self):
        return self.stack1 == []

    def size(self):
        return len(self.stack1)

    def __repr__(self):
        return str(list(reversed(self.stack1)))

queue = Queue()

queue.enqueue(1)
print(queue)

queue.enqueue(2)
queue.enqueue(3)
print(queue)

queue.dequeue()
print(queue)