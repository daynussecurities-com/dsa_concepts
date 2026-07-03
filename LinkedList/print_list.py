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

    def print_list(self):
        temp_value = self.head

        while temp_value is not None:
            print(temp_value.value)
            temp_value = temp_value.next

my_list = LinkedList(5)

my_list.print_list()