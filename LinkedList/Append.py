class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_item(self):
        list_data = self.head
        while list_data is not None:
            print(list_data.value)
            list_data = list_data.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

my_list = ListedList(2)
my_list.append(9)
my_list.append(4)
my_list.append(3)
my_list.print_item()
