class ListNode:
    
    # Singly Linked List Node structure. Value + Pointer
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    # Initializes empty LinkedList with one dummy node pointing to itself
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    # Retrieve value at i-th index
    def get(self, index: int) -> int:
        curr = self.head.next # Start at node AFTER dummy node
        i = 0 # Pointer to compare index values
        while curr: # While node is non-null
            if i == index: # Check for index match
                return curr.val # Rreturn value
            i += 1 # Keep going, no match found
            curr = curr.next # Change to next node
        return -1 # While loop done. No match found. OOB.

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) # Create new node with value
        new_node.next = self.head.next # Point node to first non-dummy node
        self.head.next = new_node # Now point dummy node to new node. [-1], [new], [2nd node]        
        
        if not new_node.next: # If empty list,
            self.tail = new_node # Point tail to itself.

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val) # Set node at end (next is null already)
        self.tail = self.tail.next # Reset tail to this node.

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False # No index at that position OOB

    def getValues(self) -> List[int]:
        curr = self.head.next
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values