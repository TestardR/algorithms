# 323. Number of connected components in undirected graph
# You have a graph of n nodes. You are given an integer n and an array edges 
# where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph. 
# Input: n = 5, edges [[0, 1], [1, 2], [3, 4]]
# Ouput: 2

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        components = 0
        
        graph = {node: [] for node in range(n)}
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        visited = set()
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        for node in graph:
            if node in visited:
                continue
            else:
                visited.add(node)
                components += 1
                dfs(node)
                
        return components
                