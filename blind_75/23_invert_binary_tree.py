# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.right, root.left = root.left, root.right
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
# T O(N)
# S O(H) Height of the tree, due to the call stack


# iterative DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            
            node.left, node.right = node.right, node.left
            
            queue.append(node.left)
            queue.append(node.right)
            
        return root
    
# T O(N)
# S O(N)
