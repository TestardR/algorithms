# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# gives root
# preorder = [3,9,20,15,7]
# from above root, we know right and left subtrees
# inorder = [9,3,15,20,7]
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0]) # 3
        mid = inorder.index(preorder[0]) # 1 
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root