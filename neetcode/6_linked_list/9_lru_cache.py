class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} # map key to node
        
        self.left = Node(0, 0) # LRU
        self.right = Node(0, 0) # MRU
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # remove from list and lete the LRU from hasmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]    