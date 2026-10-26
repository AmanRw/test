class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, data):
        # 1. Create a dummy node that points to the real head
        dummy = Node(0)
        dummy.next = self.head
        
        # 2. Traverse to the node immediately BEFORE the insertion point
        curr = dummy
        for _ in range(index):
            if curr.next is None:  # Optional: Prevents out-of-bounds errors
                break
            curr = curr.next
            
        # 3. Perform a standard middle-insertion
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node
        
        # 4. Update the real head of the list
        self.head = dummy.next
