# Problem: Given a string of opening and closing parentheses, check whether it’s balanced.
# We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets:
# {}. Assume that the string doesn’t contain any other character than these, no spaces words
# or numbers. As a reminder, balanced parentheses require every opening parenthesis to be
# closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

def reversed_par(char):
    if char == ')':
        return '('
    if char == '}':
        return '{'
    if char == ']':
        return '['

    return ''


class BalancedStack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        if not self.is_empty():
            if reversed_par(item) == self.peek():
                self.pop()
                return

        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)


def balance_check(string):
    if len(string) % 2 != 0:
        return False

    stack = BalancedStack()

    for char in string:
        stack.push(char)

    if stack.is_empty():
        return True

    return False

# Another Solution
def balance_check2(string):
    opening = ('{', '[', '(')
    stack = []

    for char in string:
        if char in opening:
            stack.append(char)
        else:
            # It means we are closing a paran. withous opening one.
            # So it should return False
            if len(stack) == 0:
                return False

            last_paran = stack.pop()

            if last_paran != reversed_par(char):
                return False

    return len(stack) == 0


print(balance_check2('[(){}]'))  # True
print(balance_check2('[]'))  # True
print(balance_check2('[](){([[[]]])}'))  # True
print(balance_check2('()(){]}'))  # False
print(balance_check2('(){[[[]{}[][]((([{}])))]]}')) #True

