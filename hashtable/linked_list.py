class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f'Node({repr(self.value)})'
class LinkedList:
    # Instantiate the Singly Linked list class
    def __init__(self):
        self.head = None
    # Create an insert method that adds a node as the head. This is a "Stack" SLL
    def insert(self, node):
        node.next = self.head
        self.head = node
    # Delete
    def delete(self, value):
        current_node = self.head
        # If you are deleting the head of the list
        if current_node.value == value:
            self.head = self.head.next
            return current_node
        # General case
        prev_node = current_node
        current_node = current_node.next
        while current_node is not None:
            if current_node.value == value:  # Delete this one
                prev_node.next = current_node.next  # Cuts out the old node
                return current_node
            else:
                prev_node = prev_node.next
                current_node = current_node.next
        return None
    def lookup(self, value):
        current_node = self.head
        # walk the linked list
        while current is not None:
            if current_node.value == value:
                # Found
                return current_node
            current_node = current_node.next
        return None