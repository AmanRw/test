class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index out of bounds")

        dummy = Node(0)
        dummy.next = self.head
        curr = dummy

        for _ in range(index):
            if curr.next is None:
                raise IndexError("Index out of bounds")
            curr = curr.next

        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

        self.head = dummy.next

    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            raise IndexError("Index out of bounds")

        dummy = Node(0)
        dummy.next = self.head
        curr = dummy

        for _ in range(index):
            if curr.next is None:
                raise IndexError("Index out of bounds")
            curr = curr.next

        if curr.next is None:
            raise IndexError("Index out of bounds")

        curr.next = curr.next.next
        self.head = dummy.next

    def delete(self, data):
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy

        while curr.next is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                self.head = dummy.next
                return True
            curr = curr.next

        self.head = dummy.next
        return False
