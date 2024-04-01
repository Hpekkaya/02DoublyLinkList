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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1
        return new_node

    def pop_first(self):
        # check length - if = 0 return None
        if self.length == 0:
            return None
        # else assign temp head
        else:
            temp = self.head
        # if = 1 head and prev None return temp
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        # else
        else:
            # assign head= head.next
            self.head = temp.next
            # head.prev = None
            self.head.prev = None
            # assign temp next None
            temp.next = None

        # Decr length
        self.length -= 1
        return temp

    def get(self, index):
        if self.length == 0:
            return None
        # Check the if index <= 0 or index >= length return None
        if (index < 0) or (index >= self.length):
            return None
        # Assign the temp->head
        # Compare the half of lenght with index
        if index < self.length:
        # less
            temp = self.head
            # start from head to index
            for _ in range(index):
                temp = temp.next
        else:
        # greater
            # backward from the tail to index
            temp = self.tail
            for _ in range((self.length-1), index-1, -1):
                tæemp = temp.prev
        return temp


my_dll = DoublyLinkedList(21)

start, end, inc = 1, 6, 1
for i in range(start, end, inc):
    my_dll.append(i)

my_dll.print_list()

index = 0

print(f"\n Index of {index} : {my_dll.get(index).value}")
