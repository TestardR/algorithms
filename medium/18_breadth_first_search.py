class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def addChild(self, name):
        self.children.append(Node(name))
    
    # O(V+E) T | O(V) S
    def breadthFirstSearch(self, array):
        queue = [self]
        
        while len(queue):
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        
        return array