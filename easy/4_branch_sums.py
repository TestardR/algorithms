class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def branch_sums(tree):
    sums = []
    compute_branch_sums(tree, 0, sums)
    return sums

# TC O(n)
# ST O(n)
def compute_branch_sums(node, running_sum, sums):
    if node is None:
        return
    
    running_sum += node.val
    
    if node.left is None and node.right is None:
        sums.append(running_sum)
        return
    
    compute_branch_sums(node.left, running_sum, sums)
    compute_branch_sums(node.right, running_sum, sums)    
    

    
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(6)
    
    print("Level order traversal: " + str(branch_sums(root)))
    
main()
    