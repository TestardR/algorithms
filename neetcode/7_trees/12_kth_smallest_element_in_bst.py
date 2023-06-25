class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.k = k
        
        # in order traversal is key
        def dfs(node):
            if not node or self.res:
                return
            
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            dfs(node.right)
            
        dfs(root)
        return self.res