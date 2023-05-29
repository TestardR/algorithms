# avg O(log(N)) worst O(N) T | recursion avg O(log(N)) worst O(N) - iteration O(1) S
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    # Avg: O(log(N)) T | O(1) S
    # Worst : O(N) T | O(1) S
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            elif value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
    
    # Avg: O(log(N)) T | O(1) S
    # Worst : O(N) T | O(1) S
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
            
        return False
    
    # Worst : O(N) T | O(N) S
    def remove(self, root, value):
        if not root:
            return root
        
        if value > root.val:
            root.right = self.remove(root.right, value)
        elif value < root.val:
            root.left = self.remove(root.left, value)
        else:
            if not root.left and not root.right:
                return None
            if not root.left and root.right:
                return root.right
            elif not root.right and root.left: 
                return root.left
            
            currNode = root.right
            while currNode.left:
                currNode = currNode.left
            root.val = currNode.val
            root.right = self.remove(root.right, root.val)
            
        return root
       