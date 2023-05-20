class Node:
    def __init__(self, val):
        self.val = val
        self.prev, self.next = None, None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def seHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.insertBefore(self.head, node)
        
    def setTail(self, node):
        if self.head is None:
            self.setHead(node)
            return
        
        self.insertBefore(self.tail, node)
        
    def insertBefore(self, node, nodeToInsert):
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
            
    def insertAfter(self, node, nodeToInsert):
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        
        if node.next is None:
            self.tail = nodeToInsert
        else: 
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
        
        
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.seHead(nodeToInsert)
            return
        
        node = self.head
        currentPosition = 1
        
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
            
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else: 
            self.setTail(nodeToInsert)
        
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove .value == value:
                self.remove(node)
        
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
            
        if node == self.tail:
            self.tail = self.tail.prev
            
        self.removeNodeBindings(node)
        
        
    def containsNodeWithValue(self, value):
        node = self.head
        
        while node is not None and node.value != value:
            node = node.next
            
        return node is not None
                
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next  
        
        if node.next is not None:
            node.next.prev = node.prev
        
        node.prev = None  
        node.next = None
                
                
        
                    
    
    
        
