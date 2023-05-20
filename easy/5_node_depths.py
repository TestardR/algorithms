class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# O(n) time | O(h) height  
def node_depths(root):
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]
    
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        
        if node is None:
            continue
        
        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sum_of_depths


# O(n) time | O(h) height   
# def node_depths(tree, depth = 0):
#     if tree is None:
#         return 0
    
#     return depth + node_depths(tree.left, depth + 1) + node_depths(tree.right, depth + 1)

    
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
    
    print("Level order traversal: " + str(node_depths(root)))
    
main()
    
    