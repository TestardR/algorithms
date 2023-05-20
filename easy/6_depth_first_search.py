class Node:
    def __init__(self, name):
        self.chidren = []
        self.name = name
        
    def add_child(self,name):
        self.chidren.append(name)
        
    # O(V + E) time | O(V) space
    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array