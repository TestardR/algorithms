class Solution:
    def validTree(self, n, edges):
        if not n:
            return True
        
        adj = {node: [] for node in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        
        def dfs(node, prevNode):
            if node in visited:
                return False
            
            visited.add(node)
            
            for neighbor in adj[node]:
                if neighbor == prevNode:
                    continue
                
                if not dfs(neighbor, node):
                    return False
                
            return True
        
        return dfs(0, -1) and n == len(visited)
        