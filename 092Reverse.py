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
        while temp is not None:
            print(f"{temp.value}", end=" ")
            temp = temp.next
        print(" ")

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

    def reverse1(self):
        # check length
        if self.length == 0:
            return None
        if self.length == 1:
            return True
        # assign head to tail and head to tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # assign and before and after
        after = temp.next
        before = None
        # Crate a loop assign, reverse then shift
        # for _ in range(self.length):
        while temp:
            after = temp.next
            # reverse
            temp.next = before
            temp.prev = after
            # shift
            before = temp
            temp = after

    def reverse(self):
        if self.length == 0: return None
        if self.length == 1: return True
        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.prev

        self.head, self.tail = self.tail, self.head




my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before reverse():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.reverse()

print('\nDLL after reverse():')
my_doubly_linked_list.print_list()
