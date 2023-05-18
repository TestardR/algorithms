class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
        
def traverse(root, sum):
    allPaths = []
    find_paths_recursive(root, sum, [], allPaths)
    return allPaths

def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    if currentNode is None:
        return
    
    currentPath.append(currentNode.val)
    
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        find_paths_recursive(currentNode.left, sum - currentNode.val, currentPath, allPaths)
        find_paths_recursive(currentNode.right, sum - currentNode.val, currentPath, allPaths)
    
    # remove the current node from the path to backtrack
    # we need to remvoe the current node while we are going up the recursive call stack.
    del currentPath[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    
    print("Tree has paths: " + str(traverse(root, 23)))
    
main()