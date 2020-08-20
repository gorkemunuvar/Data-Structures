class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        curr_node = self.head

        while curr_node:
            if curr_node.data == prev_node:
                next_node = curr_node.next
                curr_node.next = new_node
                new_node.next = next_node
                return

            curr_node = curr_node.next

    def delete_node(self, data):
        curr_node = self.head

        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            del curr_node
            return

        while curr_node.next and curr_node.next.data != data:
            curr_node = curr_node.next

        if curr_node.next is None:
            print("Couldn't find the element on the list.")
            return

        temp_node = curr_node.next
        curr_node.next = temp_node.next
        del temp_node

    def delete_node_at_position(self, position):
        curr_node = self.head

        if position == 0 and self.head != None:
            self.head = curr_node.next
            del curr_node
            return

        counter = 0
        prev_node = None
        while curr_node and counter != position:
            prev_node = curr_node
            curr_node = curr_node.next
            counter = counter + 1

        prev_node.next = curr_node.next
        del curr_node


llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.prepend("E")

llist.insert_after_node("C", "Ç")

llist.delete_node("K")
llist.delete_node("Ç")

llist.delete_node_at_position(2)

llist.print_list()
