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
                temp = temp.prev
        return temp

    def set(self, index, value):
        # check length if 0 return None
        if self.length == 0:
            return None
        # check index<0 or >= length return None
        if index < 0 or index >= self.length:
            return None

        # check index half of length
        if index < self.length/2:
        # less : iterate from head to index
            # assign temp to head of LL
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
            return temp
        else:
        # grater : iterate from tail to index
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
            temp.value = value
            return temp

        # change the node value
        # return temp

    def set1(self, index, value):
        # get the Node index with the help of get method
        temp = self.get(index)
        # change the value
        if temp:
            temp.value = value
            return temp
        return False






my_dll = DoublyLinkedList(21)

start, end, inc = 1, 6, 1
for i in range(start, end, inc):
    my_dll.append(i)

my_dll.print_list()

index, value = -1, 18
if index < 0 or index >= my_dll.length:
    print(f"{index} out of range of length of Link List")
else:
    print(f"\n The Index of {index} new value : {my_dll.set1(index, value).value}")
    my_dll.print_list()


