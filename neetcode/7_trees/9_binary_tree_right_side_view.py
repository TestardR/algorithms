# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = deque([root])
        
        while q:
            rightSide = None
            sideLevel = len(q)
            
            for _ in range(sideLevel):
                node = q.popLeft()
                
                if node: 
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightSide:
                res.append(rightSide.val)
                
        return res
                    
                    
        