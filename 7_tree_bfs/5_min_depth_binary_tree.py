from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
def traverse(root):
    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)
    minimumTreeDepth = 0
    
    while queue:
        minimumTreeDepth += 1
        levelSize = len(queue)
        
        for _ in range(levelSize):
            currentNode = queue.popleft()
            
            if not currentNode.left and not currentNode.right:
                return minimumTreeDepth
            
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right) 

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    
    print("Minimum depth: " + str(traverse(root)))
    
main()