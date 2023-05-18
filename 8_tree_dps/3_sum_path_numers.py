class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None
        
def traverse(root):
   return find_root_to_leaf_path_numbers(root, 0)

def find_root_to_leaf_path_numbers(currentNode, pathSum):
    if currentNode is None:
        return 0
    
    pathSum = 10 * pathSum + currentNode.val
    
    if currentNode.left is None and currentNode.right is None:
        return pathSum
    
    return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)



def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    
    print("Total sum of path numbers: " + str(traverse(root)))
    
main()