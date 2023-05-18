class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
        
def traverse(root, sum):
    return find_paths_recursive(root, sum, [])

def find_paths_recursive(currentNode, sum, currentPath):
    if currentNode is None:
        return 0
    
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0
    
    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]
        
        if pathSum == sum:
            pathCount += 1
            
    pathCount += find_paths_recursive(currentNode.left, sum, currentPath)
    pathCount += find_paths_recursive(currentNode.right, sum, currentPath)
    
    del currentPath[-1]
    
    return pathCount
    


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    print("Tree has paths: " + str(traverse(root, 11)))
    
main()