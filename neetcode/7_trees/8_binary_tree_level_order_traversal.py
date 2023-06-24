from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue = deque([root]) 
        res = []
        
        while queue:
            cur_level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
                cur_level.append(node.val)
                
            res.append(cur_level)
        return res