class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(f"Peeked: {stack.peek()}")
print(f"Size of Stack: {stack.size()}")

print(f"Popped: {stack.pop()}")
print(f"Size of Stack: {stack.size()}")
