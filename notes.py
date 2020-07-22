### GENERAL LECTURE NOTES

# Node

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return self.value

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

# Linked List

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if not self.tail:
            # set the new node as the tail if the list is currently empty
            self.tail = new_node
    
    def add_to_tail(self, value):
        new_node = Node(value)
        self.tail.set_next(new_node)
        self.tail = new_node
        if not self.head:
            # set the new node as the head if the list is currently empty
            self.head = new_node
    
    def remove_head(self):
        if not self.head:
            # the list is already empty
            return None

        self.head = self.head.next
        if not self.head:
            # the one and only item in the list was removed
            self.tail = None

    def remove_tail(self):
        if not self.head:
            # the list is already empty
            return None
        
        curr = self.head
        prev = curr
        while curr.get_next() != None:
            prev = curr
            curr = curr.get_next()
        
        prev.set_next(None)
        self.tail = prev