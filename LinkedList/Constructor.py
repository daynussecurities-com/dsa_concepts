class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_list = LinkedList(5)
print(my_list.head.value)
print(my_list.tail.value)
print(type(my_list))