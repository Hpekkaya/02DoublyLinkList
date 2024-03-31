class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        print("Link List :")
        while temp:
            print(f" {temp.value}", end=" ")
            temp = temp.next
        print(f"\n List Length : {self.length}")

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        # Check whether length of LL =0 return None
        if self.length == 0:
            return None
        # Create temp and assign the tail Node
        temp = self.tail
        # Check whether one node in LL
        if self.length == 1:
            self.head = None
            self.tail = None
        # Pop the last Node
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None

        # decrm the length and return temp
        self.length -= 1
        return temp



my_dll = DoublyLinkedList(0)

start, end, inc = 1, 6, 1
for i in range(start, end, inc):
    my_dll.append(i)

print("Before the Pop :" )
my_dll.print_list()

print(f"The poped : {my_dll.pop().value}")

print("After the last pop :")
my_dll.print_list()