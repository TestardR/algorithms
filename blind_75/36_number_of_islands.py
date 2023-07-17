class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid and not grid[0]:
            return

        islands = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r, c):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or (r, c) in visited
                or grid[r][c] == "0"
            ):
                return
            
            visited.add(r, c)
            
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        
        for r in ROWS:
            for c in COLS:
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        
        return islands
    
# O(n * m * 4)